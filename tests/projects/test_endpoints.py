import time
from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.project_schema import ProjectSchema


data = {
    'title': 'Title #3',
    'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                   "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of "
                   "type and scrambled it to make a type specimen book. It has survived not only five centuries, "
                   "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                   "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                   "and more recently with desktop publishing software like Aldus PageMaker including versions of "
                   "Lorem Ipsum",
    'image_path': '177283-anime-v_dayz_anime-multik-ryomen_ego_nogi-yudzi_itadori-2560x1440.jpg',
    'created_on': datetime.now(),
    'url': 'https://some_site.com'
}


@pytest.mark.anyio
async def test_get_projects(db_session: AsyncSession, client: AsyncClient):
    response = await client.get('/projects')

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response:
        assert all(isinstance(project, ProjectSchema) for project in response.json())

