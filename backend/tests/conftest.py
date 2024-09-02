from unittest.mock import MagicMock

import pytest
from httpx import AsyncClient

from app import app
from depends import get_session
from tests.test_database import override_get_db, init_db, test_async_session, drop_db


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
async def db_session():
    await init_db()
    app.dependency_overrides[get_session] = override_get_db
    async with test_async_session() as session:
        yield session
    await drop_db()


@pytest.fixture(scope="session")
async def client(db_session):
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_request() -> MagicMock:
    mock_request = MagicMock()
    mock_request.base_url = "http://test"
    return mock_request
