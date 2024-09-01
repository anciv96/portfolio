from sqlalchemy import Column, Integer, String, Boolean

from models.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return str(self.username)
