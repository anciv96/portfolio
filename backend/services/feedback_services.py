import logging

from schemas.feedback_schema import FeedbackSchema
from repositories.feedback_repository import FeedbackRepository


logger = logging.getLogger(__name__)


class FeedbackService:
    """Вся бизнес-логика системы постинга отзывов должна быть тут"""
    def __init__(self, repository: FeedbackRepository) -> None:
        self.repository = repository

    async def get_feedbacks(self) -> list[FeedbackSchema]:
        """Обрабатывает все полученные из бд данные"""
        result = await self.repository.get_feedbacks()
        return result

