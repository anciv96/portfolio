from sqlalchemy import Column, Integer, String, Text

from models.database import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    project_type = Column(String(10), nullable=True)
    budget = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    tor_file = Column(String(255), nullable=True)
    customer_name = Column(String(50), nullable=False)
    customer_number = Column(String(50), nullable=False)
    customer_email = Column(String, nullable=False)

    def __repr__(self) -> str:
        return str(f'{self.customer_name} - {self.project_type}')
