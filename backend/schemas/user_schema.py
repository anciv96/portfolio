from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    hashed_password: str
    is_admin: bool

    class Config:
        orm_mode = True
        from_attributes = True
