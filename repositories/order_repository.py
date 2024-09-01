import logging

from sqlalchemy.exc import StatementError
from sqlalchemy.ext.asyncio import AsyncSession

from models.order_model import Order
from schemas.order_schema import OrderSchema


logger = logging.getLogger(__name__)


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order(self, order: OrderSchema, tor_file_path=None) -> Order | None:
        """Создает новый заказ в базе данных."""
        try:
            new_order = Order(
                project_type=order.project_type,
                budget=order.budget,
                description=order.description,
                tor_file=tor_file_path,
                customer_name=order.customer_name,
                customer_number=order.customer_number,
                customer_email=str(order.customer_email),
            )
            self.session.add(new_order)
            await self.session.commit()
            return new_order
        except StatementError as error:
            await self.session.rollback()
            logger.error(f"Error creating order: {error}")
