import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.feedback_repository import FeedbackRepository
from schemas.feedback_schema import FeedbackSchema
from services.feedback_services import FeedbackService

data = {
    "id": 1000,
    "author": "testuserservice",
    "text": "some interesting feedback from customer",
    "url": "https://www.youtube.com/"
}


@pytest.mark.anyio()
async def test_get_feedbacks_service(client: AsyncClient, db_session: AsyncSession):
    repository = FeedbackRepository(db_session)
    service = FeedbackService(repository)

    new_feedback = FeedbackSchema(**data)
    await db_session.execute(
        text('INSERT INTO feedback(id, author, text, url) '
             'VALUES(:id, :author, :text, :url)'),
        data
    )

    feedbacks = await service.get_feedbacks()

    assert isinstance(feedbacks, list)
    assert new_feedback in feedbacks
