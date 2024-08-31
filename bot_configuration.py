from io import BytesIO

from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InputFile, FSInputFile

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def send_message(chat_id: int, message: str, document=None) -> None:
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
