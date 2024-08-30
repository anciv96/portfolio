from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config
from models.database import Base

TEST_DATABASE_URL = f'postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/test_portfolio'
test_engine = create_async_engine(TEST_DATABASE_URL)
test_async_session = async_sessionmaker(test_engine,
                                        expire_on_commit=False,
                                        )


async def override_get_db():
    async with test_async_session() as session:
        yield session
        await session.close()


async def init_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
