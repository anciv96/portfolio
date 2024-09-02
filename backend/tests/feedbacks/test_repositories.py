import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.feedback_repository import FeedbackRepository
from schemas.feedback_schema import FeedbackSchema

data = {
    "id": 10,
    "author": "test_user_repository",
    "text": "some interesting feedback from customer",
    "url": "https://www.youtube.com/"
}


@pytest.mark.anyio
async def test_get_feedbacks_repository(client: AsyncClient, db_session: AsyncSession):
    repository = FeedbackRepository(db_session)

    new_feedback = FeedbackSchema(**data)
    await db_session.execute(
        text('INSERT INTO feedback(id, author, text, url) '
             'VALUES(:id, :author, :text, :url)'),
        data
    )

    all_feedbacks_in_db = await repository.get_feedbacks()

    assert all_feedbacks_in_db is not None
    assert isinstance(all_feedbacks_in_db, list)
    assert new_feedback in all_feedbacks_in_db
