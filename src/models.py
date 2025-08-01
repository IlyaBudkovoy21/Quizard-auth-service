from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean, func
from datetime import datetime

from src.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "Users"

    username: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
