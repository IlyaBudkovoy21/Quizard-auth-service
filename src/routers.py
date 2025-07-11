from fastapi import APIRouter


router = APIRouter(prefix="/auth/v1/")


@router.post("/login")
def login():
    pass
