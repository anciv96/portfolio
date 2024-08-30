import asyncio

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

data = {
    "id": 100,
    "author": "testuser",
    "text": "some interesting feedback from customer",
    "url": "https://www.youtube.com/"
}


@pytest.mark.anyio
async def test_get_feedbacks(client: AsyncClient, db_session: AsyncSession):

    await db_session.execute(
        text('INSERT INTO feedback(id, author, text, url) '
             'VALUES(:id, :author, :text, :url)'),
        data
    )
    await db_session.commit()

    response = await client.get('/feedbacks')

    assert response.status_code == 200
    assert data in response.json()
