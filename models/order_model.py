from sqlalchemy import Column, Integer, String, Text

from models.database import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    project_type = Column(String(10))
    budget = Column(String(50))
    description = Column(Text)
    tor_file = Column(String(255))
    customer_name = Column(String(50))
    customer_number = Column(String(50))
    customer_email = Column(String)

    def __repr__(self) -> str:
        return str(f'{self.customer_name} - {self.project_type}')
