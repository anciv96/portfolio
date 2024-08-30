from pydantic import BaseModel, HttpUrl, Field


class ProjectSchema(BaseModel):
    id: int
    title: str = Field(examples=["Интернет магазин"])
    description: str = Field(examples=["Интернет магазин для продажи драгоценных услуг"])
    image_path: str
    url: HttpUrl = Field(examples=["https://link_to_site"])

    class Config:
        orm_mode = True
        from_attributes = True
