import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from starlette.responses import FileResponse

from schemas.project_schema import ProjectSchema
from services.project_services import ProjectService
from depends import get_project_repository, get_project_service


router = APIRouter(prefix='/projects', tags=['Project'])
logger = logging.getLogger(__name__)


@router.get('')
async def get_projects(
        request: Request,
        project_service: Annotated[ProjectService, Depends(get_project_service)]
) -> list[ProjectSchema]:
    """Получает все проекты из базы данных"""
    try:
        projects = await project_service.get_projects(request)
        return projects
    except Exception as error:
        logger.error(error)


@router.get("/{project_id}/image/")
async def get_project_image(project_id: int,
                            project_service: Annotated[ProjectService, Depends(get_project_repository)]
                            ):
    """Получает изображение на конкретный проект"""
    try:
        project = await project_service.get_project(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        return FileResponse(project.image_path)
    except Exception as error:
        logging.error(error)
