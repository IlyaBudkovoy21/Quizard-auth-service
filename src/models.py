from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean, func
from uuid import UUID
from datetime import datetime

from src.config.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "Users"

    username: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
