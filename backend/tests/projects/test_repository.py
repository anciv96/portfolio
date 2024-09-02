import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.project_repository import ProjectRepository


data = {
    'title': 'Title #2',
    'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                   "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of "
                   "type and scrambled it to make a type specimen book. It has survived not only five centuries, "
                   "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                   "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                   "and more recently with desktop publishing software like Aldus PageMaker including versions of "
                   "Lorem Ipsum",
    'image_path': '55555555.png',
    'created_on': datetime.datetime.now(),
    'url': 'https://some_site.com'
}


@pytest.mark.anyio
async def test_get_all_projects_repository(db_session: AsyncSession, client: AsyncClient):
    project_repository = ProjectRepository(db_session)

    await db_session.execute(
        text('INSERT INTO project(title, description, url, created_on, image_path) '
             'VALUES(:title, :description, :url, :created_on, :image_path)'),
        data
    )

    all_projects_in_db = await project_repository.get_projects()

    assert all_projects_in_db is not None
    assert isinstance(all_projects_in_db, list)


