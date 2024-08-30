from sqlalchemy import Text, Column, String, Integer

from models.database import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    author = Column(String(50))
    text = Column(Text())
    url = Column(String())

    def __repr__(self) -> str:
        return f'{self.id}:{self.author}'
