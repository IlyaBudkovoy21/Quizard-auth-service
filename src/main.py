from fastapi import FastAPI
from fastapi_users import FastAPIUsers

import uuid

from src.models import User
from src.routers import router


app = FastAPI()

app.include_router(router)



