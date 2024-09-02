from io import BytesIO

import pytest
from fastapi import UploadFile
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderSchema
from services.order_services import OrderService

order_data = {
    'project_type': 'Сайт',
    'budget': '50-100 тыс. рублей',
    'description': 'Lorem Ipsum dolor upset...',
    'customer_name': 'Lee',
    'customer_number': '+998 99 123 45 67',
    'customer_email': 'lee@gmail.com'
}


async def create_order(service, tor_file: UploadFile) -> None:
    new_order = OrderSchema(**order_data)
    await service.create_order_and_send_message(new_order, tor_file)


@pytest.mark.anyio
async def test_create_order_service(client: AsyncClient, db_session: AsyncSession):
    repository = OrderRepository(db_session)
    service = OrderService(repository)

    test_file_content = b"Test file content"
    test_file = UploadFile(
        filename="test_file.txt",
        file=BytesIO(test_file_content)
    )

    await create_order(service, tor_file=test_file)



