import logging

import bcrypt
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from exceptions.user_exceptions import UserNotFoundError
from repositories.user_repository import UserRepository
from schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


class AdminAuth(AuthenticationBackend):
    """
    Класс аутентификации для админ-панели, использующий хэширование паролей и сессии.
    """
    def __init__(self,
                 secret_key: str,
                 user_repository: UserRepository,
                 ):
        super().__init__(secret_key)
        self.user_repository = user_repository
        self.password_service = PasswordService()
        self.session_service = SessionService()

    async def login(self, request: Request) -> bool:
        """
        Аутентифицирует пользователя на основе введённых данных.

        Args:
            request (Request): Объект запроса, содержащий форму с данными пользователя.

        Returns:
            bool: return True, если аутентификация успешна и пользователь является администратором, иначе False.
        """
        form = await request.form()
        user = await self._get_user(form['username'])

        if user and self.password_service.verify_password(form['password'], user.hashed_password):
            if user.is_admin:
                self.session_service.update_user_session(request, user.username)
                return True
        return False

    async def logout(self, request: Request) -> bool:
        """
        Завершает сессию пользователя, очищая сессию.

        Args:
            request (Request): Объект запроса, содержащий сессию.

        Returns:
            bool: Всегда return True после завершения сессии.
        """
        self.session_service.clear_session(request)
        return True

    async def authenticate(self, request: Request) -> bool:
        """
        Проверяет, аутентифицирован ли текущий пользователь.

        Args:
            request (Request): Объект запроса, содержащий сессию.

        Returns:
            bool: return True, если пользователь аутентифицирован, иначе False.
        """
        return self.session_service.is_authenticated(request)

    async def _get_user(self, username: str) -> UserSchema | None:
        try:
            return await self.user_repository.get_user(username)
        except UserNotFoundError:
            logger.warning(f"User '{username}' not found")
            return None


class PasswordService:
    """Сервис для работы с паролями, включающий проверку пароля."""
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Сравнивает обычный пароль с его хешем.

        Args:
            plain_password (str): Обычный пароль, введённый пользователем.
            hashed_password (str): Хешированный пароль, сохранённый в базе данных.

        return:
            bool: return True, если пароль совпадает с хешем, иначе False.
        """
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


class SessionService:
    """Сервис для работы с сессиями, включающий управление и проверку сессий."""

    @staticmethod
    def update_user_session(request: Request, username: str) -> None:
        """
        Обновляет сессию пользователя, сохраняя имя пользователя в сессии.

        Args:
            request (Request): Объект запроса, содержащий сессию.
            username (str): Имя пользователя, которое будет сохранено в сессии.
        """
        request.session.update({"token": username})

    @staticmethod
    def clear_session(request: Request) -> None:
        """
        Очищает текущую сессию пользователя.

        Args:
            request (Request): Объект запроса, содержащий сессию.
        """
        request.session.clear()

    @staticmethod
    def is_authenticated(request: Request) -> bool:
        """
        Проверяет, аутентифицирован ли пользователь на основе сессии.

        Args:
            request (Request): Объект запроса, содержащий сессию.

        return:
            bool: return True, если пользователь аутентифицирован, иначе False.
        """
        return request.session.get("token") is not None

