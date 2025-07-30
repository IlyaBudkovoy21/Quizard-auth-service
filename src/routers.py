from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select
from status import HTTP_201_CREATED, HTTP_409_CONFLICT
from passlib.context import CryptContext

from src.config.database import get_async_session, AsyncSession
from src.models import User
from src.schemas import UserRegistrationData


router = APIRouter(prefix="/auth/v1/")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/registration", status_code=HTTP_201_CREATED)
async def registration(user_data: UserRegistrationData, session: AsyncSession = Depends(get_async_session)):
    pass

    # hashed_password = pwd_context.hash(user_data.password)



@router.post("/login")
def login():
    pass
