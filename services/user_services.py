import logging

import bcrypt
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from exceptions.user_exceptions import UserNotFoundError
from repositories.user_repository import UserRepository
from schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


class PasswordService:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


class SessionService:
    @staticmethod
    def update_user_session(request: Request, username: str) -> None:
        request.session.update({"token": username})

    @staticmethod
    def clear_session(request: Request) -> None:
        request.session.clear()

    @staticmethod
    def is_authenticated(request: Request) -> bool:
        return request.session.get("token") is not None


class AdminAuth(AuthenticationBackend):
    def __init__(self,
                 secret_key: str,
                 user_repository: UserRepository,
                 ):
        super().__init__(secret_key)
        self.user_repository = user_repository
        self.password_service = PasswordService()
        self.session_service = SessionService()

    async def login(self, request: Request) -> bool:
        form = await request.form()
        user = await self._get_user(form['username'])

        if user and self.password_service.verify_password(form['password'], user.hashed_password):
            if user.is_admin:
                self.session_service.update_user_session(request, user.username)
                return True
        return False

    async def logout(self, request: Request) -> bool:
        self.session_service.clear_session(request)
        return True

    async def authenticate(self, request: Request) -> bool:
        return self.session_service.is_authenticated(request)

    async def _get_user(self, username: str) -> UserSchema | None:
        try:
            return await self.user_repository.get_user(username)
        except UserNotFoundError:
            logger.warning(f"User '{username}' not found")
            return None
