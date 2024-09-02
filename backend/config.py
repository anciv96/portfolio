from dotenv import load_dotenv
import os


load_dotenv()

JWT_KEY = os.environ.get('JWT_KEY')

ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

PROJECT_IMAGES_UPLOAD_DIR = 'uploads/projects'
ORDER_FILES_UPLOAD_DIR = 'uploads/tor_files'

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_ID')

