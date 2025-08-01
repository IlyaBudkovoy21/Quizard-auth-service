import uuid
from datetime import datetime
from pydantic import ConfigDict

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
