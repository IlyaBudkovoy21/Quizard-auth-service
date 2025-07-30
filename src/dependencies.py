from fastapi import Depends

from src.config.database import AsyncSession, get_async_session
from src.validators import UserCreateValidator


async def get_user_validator(session: AsyncSession = Depends(get_async_session)) -> UserCreateValidator:
    """Returns the UserCreateValidator instance with the injected session"""
    return UserCreateValidator(session)
