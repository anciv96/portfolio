import logging.config

from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {
            "level": "WARNING",
            "handlers": ["file"],
        },
    },
}
logging.config.dictConfig(LOGGING_CONFIG)


bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
