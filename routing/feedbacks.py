import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from services.feedback_services import FeedbackService
from schemas.feedback_schema import FeedbackSchema
from depends import get_feedback_service

router = APIRouter(prefix='/feedbacks', tags=['Feedback'])
logger = logging.getLogger(__name__)


@router.get('')
async def get_feedbacks(
        feedback_service: Annotated[FeedbackService, Depends(get_feedback_service)]
) -> list[FeedbackSchema]:
    """
    Получает все отзывы заказчиков из базы данных.
    """
    try:
        feedbacks = await feedback_service.get_feedbacks()
        return feedbacks
    except Exception as error:
        logger.error(f"Error while retrieving feedbacks: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving feedbacks."
        )
