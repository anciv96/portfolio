import logging

import bcrypt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from exceptions.user_exceptions import UserNotFoundError
from models.user_model import User
from schemas.user_schema import UserSchema


logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user: UserSchema):
        hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())
        admin_user = User(
            username=user.username,
            hashed_password=hashed_password.decode('utf-8'),
            email=user.email,
            is_admin=user.is_admin,
        )
        self.session.add(admin_user)
        await self.session.commit()
        return admin_user

    async def get_user(self, username: str) -> UserSchema:
        user_object = await self.session.execute(
            select(User).where(User.username == username)
        )
        user = user_object.scalars().first()
        try:
            result = UserSchema(
                email=user.email,
                username=user.username,
                hashed_password=user.hashed_password,
                is_admin=user.is_admin
            )

            return result
        except AttributeError as error:
            logger.exception(error)
            raise UserNotFoundError(error)
