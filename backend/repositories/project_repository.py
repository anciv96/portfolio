import logging
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.project_schema import ProjectSchema
from models.project_model import Project


logger = logging.getLogger(__name__)


class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_projects(self) -> Sequence:
        """Получает все проекты с базы данных"""
        try:
            response = await self.session.execute(select(Project))
            projects = response.scalars().all()

            return projects
        except Exception as error:
            logging.error(error)

    async def get_project(self, project_id: int) -> ProjectSchema | None:
        """Получает проект по ID из базы данных.

        Args:
            project_id (int): id проекта.

        Returns:
            ProjectSchema: Схема, представляющая проект.
        """
        try:
            project = await self.session.get(Project, project_id)
            if project:
                result = ProjectSchema(
                    id=project.id,
                    title=project.title,
                    description=project.description,
                    url=project.url,
                    image_path=project.image_path
                )
                return result
        except Exception as error:
            logger.error(error)
