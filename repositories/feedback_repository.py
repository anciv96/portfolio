import logging

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.feedback_schema import FeedbackSchema
from models.feedback_model import Feedback


logger = logging.getLogger(__name__)


class FeedbackRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_feedbacks(self) -> list[FeedbackSchema]:
        """Получает все данные из базы данных"""
        try:
            response = await self.session.execute(select(Feedback))
            feedbacks = response.scalars().all()
            result = [FeedbackSchema.from_orm(feedback) for feedback in feedbacks]
            return result
        except InvalidRequestError as error:
            logger.error(error)

