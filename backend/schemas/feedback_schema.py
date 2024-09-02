from pydantic import BaseModel, HttpUrl, Field


class FeedbackSchema(BaseModel):
    id: int
    author: str = Field(examples=['James Moriarty'])
    text: str = Field(examples=['Everything is great, prompt on time, high quality. Thank you! Recommended'])
    url: HttpUrl

    class Config:
        orm_mode = True
        from_attributes = True
