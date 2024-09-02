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
    """
    Сервис для работы с заказами.
    Обрабатывает создание заказов и отправку уведомлений через Telegram.
    """
    def __init__(self, repository: OrderRepository):
        self.repository = repository
        self.file_service = FileService()
        self.notification_service = NotificationService()

    async def create_order_and_send_message(self, order: OrderSchema, tor_file: UploadFile = None):
        """
        Создает заказ в базе данных и отправляет уведомление в Telegram.

        Args:
            order (OrderSchema): Данные заказа.
            tor_file (UploadFile, optional): Файл технического задания для сохранения. По умолчанию None.

        Raises:
            OrderTorFileNotFoundError: Если файл не найден.
            OrderTorFilePermissionError: Если у программы нет прав на сохранение файла.
            OrderTorFileIOError: Если произошла ошибка ввода-вывода при сохранении файла.
        """
        file_location = await self.file_service.save_file(ORDER_FILES_UPLOAD_DIR, tor_file) if tor_file else None

        message_text = await self.notification_service.create_message_text(order)
        await self.notification_service.telegram_notifier(CHAT_ID, message_text, document=file_location)

        await self.repository.create_order(order, file_location)


class NotificationService:
    """
    Сервис для отправки уведомлений о новых заказах.
    """
    @staticmethod
    async def create_message_text(order: OrderSchema) -> str:
        """
        Формирует текст уведомления на основе данных заказа.

        Args:
            order (OrderSchema): Данные заказа.

        Returns:
            str: Текст уведомления для отправки в Telegram.
        """
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
    async def telegram_notifier(chat_id: int, message: str, document: str | bytes = None) -> None:
        """
        Отправляет уведомление в Telegram.

        Args:
            chat_id (int): Идентификатор чата в Telegram.
            message (str): Текст уведомления.
            document (str | bytes, optional): Путь к файлу или бинарные данные для отправки в Telegram. По умолчанию None.
        """
        if document:
            input_file = FSInputFile(document)
            await bot.send_document(chat_id=chat_id, document=input_file, caption=message)
        else:
            await bot.send_message(chat_id=chat_id, text=message)


class FileService:
    """
    Сервис для работы с файлами, включая сохранение файлов на сервере.
    """
    async def save_file(self, upload_dir: str, tor_file: UploadFile) -> str:
        """
        Сохраняет файл технического задания (ТЗ) в указанную директорию.

        Args:
            upload_dir (str): Директория для сохранения файла.
            tor_file (UploadFile): Загруженный файл для сохранения.

        Returns:
            str: Путь к сохраненному файлу.

        Raises:
            OrderTorFileNotFoundError: Если файл не найден.
            OrderTorFilePermissionError: Если у программы нет прав на сохранение файла.
            OrderTorFileIOError: Если произошла ошибка ввода-вывода при сохранении файла.
        """
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
