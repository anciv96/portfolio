import logging
from typing import Annotated, Literal

from fastapi import APIRouter, UploadFile, Depends, Form, File

from depends import get_order_service
from schemas.order_schema import OrderSchema
from services.order_services import OrderService

router = APIRouter(prefix='/order')
logger = logging.getLogger(__name__)


@router.post('')
async def order(
    order_service: Annotated[OrderService, Depends(get_order_service)],
    project_type: Literal['Сайт', 'Чат-бот'] = Form(...),
    budget: Literal[
        '50-100 тыс. рублей',
        '100-300 тыс. рублей',
        '300-500 тыс. рублей',
        '500+ тыс. рублей'
    ] = Form(...),
    description: str = Form(...),
    customer_name: str = Form(...),
    customer_number: str = Form(...),
    customer_email: str = Form(...),
    tor_file: UploadFile = File(None),
):
    # TODO check if order_service is required in ui
    new_order = OrderSchema(
        project_type=project_type,
        budget=budget,
        description=description,
        customer_name=customer_name,
        customer_number=customer_number,
        customer_email=customer_email,
    )

    await order_service.create_order(new_order, tor_file=tor_file)

    return new_order

