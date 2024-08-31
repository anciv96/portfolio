import logging
import os.path

from aiofiles import open as async_open
from aiogram.types import FSInputFile
from fastapi import UploadFile

from config import ORDER_FILES_UPLOAD_DIR, CHAT_ID
from dispatcher import bot
from exceptions.order_exceptions import OrderTorFileNotFoundError, OrderTorFilePermissionError, OrderTorFileIOError
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderSchema


logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    async def create_order(self, order: OrderSchema, tor_file: UploadFile = None):
        try:
            file_location = await self._save_file_to_server(tor_file) if tor_file else None

            message_text = await self._create_message_text(order)
            await self._send_message(CHAT_ID, message_text, document=file_location)

        except (OrderTorFileNotFoundError, OrderTorFilePermissionError, OrderTorFileIOError):
            file_location = None

        await self.repository.create_order(order, file_location)

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


    async def _create_message_text(self, order: OrderSchema) -> str:
        message = ['Новый заказ\n\n']

        await self._check_if_attribute_exists(message, pre='<b>Тип проекта</b>', attribute=order.project_type)
        await self._check_if_attribute_exists(message, pre='<b>Бюджет</b>', attribute=order.budget)
        await self._check_if_attribute_exists(message, pre='<b>Описание</b>', attribute=order.description)
        await self._check_if_attribute_exists(message, pre='<b>Имя заказчика</b>', attribute=order.customer_name)
        await self._check_if_attribute_exists(message, pre='<b>Номер заказчика</b>', attribute=order.customer_number)
        await self._check_if_attribute_exists(message, pre='<b>Email заказчика</b>', attribute=order.customer_email)

        return message[0]

    @staticmethod
    async def _check_if_attribute_exists(message: list, pre: str, attribute):
        # TODO rename
        try:
            message[0] += f'{pre}: {attribute}\n'
        except AttributeError as error:
            logger.error(error)

    @staticmethod
    async def _send_message(chat_id: int, message: str, document=None) -> None:
        if document:
            input_file = FSInputFile(document)

            await bot.send_document(
                chat_id=chat_id,
                document=input_file,
                caption=message
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=str(message)
            )

