import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from services.feedback_services import FeedbackService
from schemas.feedback_schema import FeedbackSchema
from depends import get_feedback_repository

router = APIRouter(prefix='/feedbacks', tags=['Feedback'])
logger = logging.getLogger(__name__)


@router.get('')
async def get_feedbacks(feedback_service: Annotated[FeedbackService, Depends(get_feedback_repository)]) \
        -> list[FeedbackSchema]:
    """Получает все отзывы заказчиков с базы данных"""
    try:
        feedbacks = await feedback_service.get_feedbacks()
        return feedbacks
    except Exception as error:
        logger.error(error)

