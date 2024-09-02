from datetime import datetime

from fastapi_storages import FileSystemStorage
from sqlalchemy import Column, Integer, String, Text, DateTime
from fastapi_storages.integrations.sqlalchemy import ImageType

from config import PROJECT_IMAGES_UPLOAD_DIR
from models.database import Base


storage = FileSystemStorage(path=PROJECT_IMAGES_UPLOAD_DIR)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=True)
    image_path = Column(ImageType(storage=storage), nullable=False)
    url = Column(String(), nullable=True)
    date = Column('created_on', DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return str(self.title)
