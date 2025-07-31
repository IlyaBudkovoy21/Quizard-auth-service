from fastapi import APIRouter, Depends, HTTPException

from status import HTTP_201_CREATED, HTTP_409_CONFLICT
from passlib.context import CryptContext

from src.config.database import get_async_session, AsyncSession
from src.schemas import UserRegistrationData
from src.dependencies import get_user_validator

router = APIRouter(prefix="/auth/v1/")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/registration", status_code=HTTP_201_CREATED)
async def registration(user_data: UserRegistrationData, session: AsyncSession = Depends(get_async_session)):
    pass


@router.post("/login")
def login():
    pass
