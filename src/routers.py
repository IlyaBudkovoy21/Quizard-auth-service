from fastapi import APIRouter, Depends

from src.verifications import get_current_user


verif_router = APIRouter()


@verif_router.get("/verify-token")
async def verify_token(user_data: dict = Depends(get_current_user)):
    return {
        "status": "success",
    }
