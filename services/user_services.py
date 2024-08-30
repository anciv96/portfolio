import logging

import bcrypt
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from exceptions.user_exceptions import UserNotFoundError
from repositories.user_repository import UserRepository
from schemas.user_schema import UserSchema


logger = logging.getLogger(__name__)


class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str, user_repository: UserRepository):
        super().__init__(secret_key)
        self.user_repository = user_repository

    @staticmethod
    async def _update_user_session(user: UserSchema, form, request: Request) -> bool:
        """Обновляет сессии пользователя, после логина"""
        if not user:
            return False

        username = form['username']
        password = form['password']

        if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            if user.is_admin:
                request.session.update({"token": username})
                return True
        return False

    async def _get_user(self, form) -> UserSchema | bool:
        try:
            user = await self.user_repository.get_user(form['username'])
            return user
        except UserNotFoundError:
            return False

    async def login(self, request: Request) -> bool:

        form = await request.form()
        user = await self._get_user(form)
        update_session = await self._update_user_session(user, form, request)
        return update_session

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        return token is not None

