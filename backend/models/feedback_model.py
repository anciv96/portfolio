from sqlalchemy import Text, Column, String, Integer

from models.database import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    text = Column(Text(), nullable=False)
    url = Column(String(), nullable=False)

    def __repr__(self) -> str:
        return f'{self.id}:{self.author}'
