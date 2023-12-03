from fastapi import APIRouter

from src.main.util.logger import logger


router = APIRouter(tags=["Admin Operations"])


@router.get("/ping", name="Health check", description="returns 200")
async def health_check():
    return {"status": "ok"}
