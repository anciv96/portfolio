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
        self.file_service = FileService()
        self.notification_service = NotificationService()

    async def create_order_and_send_message(self, order: OrderSchema, tor_file: UploadFile = None):
        file_location = await self.file_service.save_file(ORDER_FILES_UPLOAD_DIR, tor_file) if tor_file else None

        message_text = await self.notification_service.create_message_text(order)
        await self.notification_service.send_message(CHAT_ID, message_text, document=file_location)
        await self.repository.create_order(order, file_location)


class NotificationService:
    @staticmethod
    async def create_message_text(order: OrderSchema) -> str:
        attributes = {
            '<b>Тип проекта</b>': order.project_type,
            '<b>Бюджет</b>': order.budget,
            '<b>Описание</b>': order.description,
            '<b>Имя заказчика</b>': order.customer_name,
            '<b>Номер заказчика</b>': order.customer_number,
            '<b>Email заказчика</b>': order.customer_email,
        }
        message = 'Новый заказ\n\n'
        for pre, attribute in attributes.items():
            if attribute:
                message += f'{pre}: {attribute}\n'
        return message

    @staticmethod
    async def send_message(chat_id: int, message: str, document: str | bytes = None) -> None:
        if document:
            input_file = FSInputFile(document)
            await bot.send_document(chat_id=chat_id, document=input_file, caption=message)
        else:
            await bot.send_message(chat_id=chat_id, text=message)


class FileService:
    async def save_file(self, upload_dir: str, tor_file: UploadFile) -> str:
        file_location = os.path.join(upload_dir, tor_file.filename)
        try:
            async with async_open(file_location, 'wb') as file:
                await file.write(await tor_file.read())
            return file_location
        except FileNotFoundError as error:
            self._handle_exception(OrderTorFileNotFoundError, error, file_location)
        except PermissionError as error:
            self._handle_exception(OrderTorFilePermissionError, error, file_location)
        except IOError as error:
            self._handle_exception(OrderTorFileIOError, error, file_location)

    @staticmethod
    def _handle_exception(exception_cls, error, file_location):
        logger.error(f'Error saving file at {file_location}: {error}')
        raise exception_cls(error)
