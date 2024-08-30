import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user_repository import UserRepository
from schemas.user_schema import UserSchema

data = {
    "username": "test_user",
    "hashed_password": "my_secret_password",
    "email": "test_user@gmail.com",
    "is_admin": True
}


@pytest.mark.anyio
async def test_add_user_repository(client: AsyncClient, db_session: AsyncSession):
    repository = UserRepository(db_session)

    new_user = UserSchema(**data)
    await repository.add_user(new_user)

    users_in_db = await db_session.execute(
        text('SELECT * FROM "user" WHERE "username"=:username'),
        {'username': data['username']}
    )
    user = users_in_db.first()

    assert user is not None
    assert user.username == data['username']


@pytest.mark.anyio
async def test_get_user_repository(client: AsyncClient, db_session: AsyncSession):
    repository = UserRepository(db_session)

    new_user = UserSchema(**data)
    await repository.add_user(new_user)

    user = await repository.get_user(new_user.username)

    assert user is not None
    assert user.username in data['username']
