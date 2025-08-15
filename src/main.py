from fastapi import FastAPI
from fastapi_users import FastAPIUsers

import uuid

from src.routers import verif_router
from src.schemas import UserRead, UserCreate
from src.config.auth import get_user_manager, auth_backend
from src.models import User


app = FastAPI()

app.include_router(verif_router)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/v1",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/v1",
    tags=["register"],
)
