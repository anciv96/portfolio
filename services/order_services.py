import logging
import os.path

from aiofiles import open as async_open
from fastapi import UploadFile

from bot_configuration import send_message
from config import ORDER_FILES_UPLOAD_DIR, CHAT_ID
from exceptions.order_exceptions import OrderTorFileNotFoundError, OrderTorFilePermissionError, OrderTorFileIOError
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderSchema


logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    @staticmethod
    async def _save_file_to_server(tor_file) -> str | bytes:
        try:
            file_location = os.path.join(ORDER_FILES_UPLOAD_DIR, tor_file.filename)
            async with async_open(file_location, 'wb') as file:
                await file.write(await tor_file.read())

            return file_location
        except FileNotFoundError as error:
            logger.error(error)
            raise OrderTorFileNotFoundError(error)
        except PermissionError as error:
            logger.error(error)
            raise OrderTorFileNotFoundError(error)
        except IOError as error:
            logger.error(error)
            raise OrderTorFileIOError(error)

    async def create_order(self, order: OrderSchema, tor_file: UploadFile = None):
        try:
            file_location = await self._save_file_to_server(tor_file) if tor_file else None

            message_text = (f'Новый заказ\n\n'
                            f'<b>Тип проекта</b>: {order.project_type}\n'
                            f'<b>Бюджет</b>: {order.budget}\n'
                            f'<b>Описание</b>: {order.description}\n'
                            f'<b>Имя заказчика</b>: {order.customer_name}\n'
                            f'<b>Номер заказчика</b>: {order.customer_number}\n'
                            f'<b>Email заказчика</b>: {order.customer_email}')
            await send_message(CHAT_ID, message_text, document=file_location)

        except (OrderTorFileNotFoundError, OrderTorFilePermissionError, OrderTorFileIOError):
            file_location = None

        await self.repository.create_order(order, file_location)
