from datetime import datetime
from unittest.mock import MagicMock, AsyncMock

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.project_repository import ProjectRepository
from schemas.project_schema import ProjectSchema
from services.project_services import ProjectService

data = {
    'title': 'Title #2',
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
async def test_get_all_projects_service(db_session: AsyncSession, client: AsyncClient, mock_request: MagicMock):
    project_repository = ProjectRepository(db_session)
    project_service = ProjectService(project_repository)

    await db_session.execute(
        text('INSERT INTO project(title, description, url, created_on, image_path) '
             'VALUES(:title, :description, :url, :created_on, :image_path)'),
        data
    )

    projects = await project_service.get_projects(mock_request)

    assert projects is not None
    assert isinstance(projects, list)
    assert all(isinstance(project, ProjectSchema) for project in projects)


@pytest.mark.anyio
async def test_get_project_service(db_session: AsyncSession, client: AsyncClient, mock_request: MagicMock):
    project_repository = ProjectRepository(db_session)
    project_service = ProjectService(project_repository)

    # Вызов метода
    await db_session.execute(
        text('INSERT INTO project(id, title, description, url, created_on, image_path) '
             'VALUES(99, :title, :description, :url, :created_on, :image_path)'),
        data
    )

    project = await project_service.get_project(99)

    assert project is not None
    assert isinstance(project, ProjectSchema)
