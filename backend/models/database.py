from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config


class Base(DeclarativeBase):
    pass


DATABASE_URL = (f'postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}@'
                f'{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')


engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
