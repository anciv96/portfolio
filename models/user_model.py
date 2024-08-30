from sqlalchemy import Column, Integer, String, Boolean

from models.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    hashed_password = Column(String)
    is_admin = Column(Boolean)

    def __repr__(self) -> str:
        return str(self.username)
