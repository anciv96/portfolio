import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from models.order_model import Order
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderSchema

order_data = {
    'project_type': 'Сайт',
    'budget': '50-100 тыс. рублей',
    'description': 'Lorem Ipsum dolor upset...',
    # 'tor_file': 'uploads/tor_files/some_tor.txt',
    'customer_name': 'Lee',
    'customer_number': '+998 99 123 45 67',
    'customer_email': 'lee@gmail.com'
}


async def get_project(db_session) -> Order:
    orders = await db_session.execute(
        text('SELECT * FROM "order" WHERE project_type=:project_type'),
        {'project_type': order_data['project_type']}
    )
    return orders.fetchone()


async def create_order(order_repository: OrderRepository, tor_file: str):
    new_order = OrderSchema(**order_data)
    await order_repository.create_order(new_order, tor_file)


@pytest.mark.anyio
async def test_create_order_repository(client: AsyncClient, db_session: AsyncSession):
    order_repository = OrderRepository(db_session)

    await create_order(order_repository, 'uploads/tor_files/some_tor.txt')
    order = await get_project(db_session)

    assert order is not None
    assert order.customer_name == order_data['customer_name']
