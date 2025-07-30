from pydantic import BaseModel, Field, EmailStr


class UserRegistrationData(BaseModel):
    username: str = Field(max_length=30)
    password: str = Field(max_length=50)
    email: EmailStr
