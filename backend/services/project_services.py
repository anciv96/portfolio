from repositories.project_repository import ProjectRepository
from schemas.project_schema import ProjectSchema


class ProjectService:
    """
    Сервис для работы с проектами в портфолио.
    Содержит методы для получения всех проектов и отдельного проекта из базы данных.
    """
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    async def get_projects(self, request) -> list[ProjectSchema]:
        """
        Получает все проекты из базы данных и возвращает их в виде списка схем.

        Args:
            request (Request): Объект запроса, используемый для генерации URL изображений.

        Returns:
            list[ProjectSchema]: Список схем, представляющих проекты.
        """
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

    async def get_project(self, project_id: int) -> ProjectSchema:
        """
        Получает определенный проект из базы данных по его идентификатору.

        Args:
            project_id (int): Идентификатор проекта.

        Returns:
            ProjectSchema: Схема, представляющая проект.
        """
        project = await self.repository.get_project(project_id)

        return project
