from sqlalchemy import select
from pydantic import EmailStr

from src.models import User
from src.base import BaseAsyncService


class UserCreateValidator(BaseAsyncService):
    async def is_exist_user(self, email: EmailStr) -> bool:
        """Checking for the user's existence by email"""
        existing_user = await self.session.execute(
            select(User).where(User.email == email)
        )
        if existing_user.scalar_one_or_none() is None:
            return False
        return True
