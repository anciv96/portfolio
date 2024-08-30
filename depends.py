from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.database import async_session
from repositories.feedback_repository import FeedbackRepository
from repositories.order_repository import OrderRepository
from repositories.project_repository import ProjectRepository
from repositories.user_repository import UserRepository
from services.order_services import OrderService
from services.project_services import ProjectService


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def get_feedback_repository(
        session: AsyncSession = Depends(get_session)
) -> FeedbackRepository:
    # TODO check for validity service layer
    return FeedbackRepository(session)


async def get_project_repository(
        session: AsyncSession = Depends(get_session)
) -> ProjectRepository:
    return ProjectRepository(session)


async def get_project_service(
        repository=Depends(get_project_repository)
) -> ProjectService:
    return ProjectService(repository)


async def get_order_repository(
        session: AsyncSession = Depends(get_session)
) -> OrderRepository:
    return OrderRepository(session)


async def get_order_service(
        repository=Depends(get_order_repository)
) -> OrderService:
    return OrderService(repository)


async def create_user_repository():
    async for session in get_session():
        user_repository = UserRepository(session)
        return user_repository
