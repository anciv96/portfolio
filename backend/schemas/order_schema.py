from typing import Literal

from fastapi import UploadFile, File
from pydantic import BaseModel, EmailStr, Field


class OrderSchema(BaseModel):
    project_type: Literal['Сайт', 'Чат-бот']
    budget: Literal[
        '50-100 тыс. рублей',
        '100-300 тыс. рублей',
        '300-500 тыс. рублей',
        '500+ тыс. рублей'
    ]
    description: str = Field(examples=['Сайт для продаж интернет услуг...'])
    customer_name: str = Field(examples=['Lee'])
    customer_number: str = Field(examples=['+998 99 123 45 67'])
    customer_email: EmailStr = Field(examples=['lee@gmail.com'])

    class Config:
        orm_mode = True
        from_attributes = True
