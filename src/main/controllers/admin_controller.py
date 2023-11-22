from fastapi import APIRouter
from pydantic import BaseModel

from src.main.util.logger import logger



router = APIRouter(tags=["Admin Controller"])


@router.get("/ping", name="Health check", description="returns 200")
async def health_check():
    return {"status": "ok"}
