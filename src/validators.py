from sqlalchemy import select

from src.models import User
from src.config.database import AsyncSession


class UserCreateValidator:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def is_exist_user(self, email: str) -> bool:
        """Checking for the user's existence by email"""
        existing_user = await self.session.execute(
            select(User).where(User.email == email)
        )
        if existing_user.scalar_one_or_none() is None:
            return False
        return True
