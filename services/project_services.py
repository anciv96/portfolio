from repositories.project_repository import ProjectRepository
from schemas.project_schema import ProjectSchema


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    async def get_projects(self, request) -> list[ProjectSchema]:
        """Получает все проекты из бд"""
        projects = await self.repository.get_projects()

        result = [
            ProjectSchema(
                id=project.id,
                title=project.title,
                description=project.description,
                url=project.url,
                image_path=f"{request.base_url}projects/{project.id}/image/"
            ) for project in projects
        ]
        return result

    async def get_project(self, project_id) -> ProjectSchema:
        project = await self.repository.get_project(project_id)

        return project
