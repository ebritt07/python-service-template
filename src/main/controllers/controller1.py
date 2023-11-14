from fastapi import APIRouter
from pydantic import BaseModel

from src.main.util.logger import logger


class Item(BaseModel):
    name: str
    price: float


router = APIRouter(tags=["Controller 1"])


@router.get("/items/{item_id}", name="Get Item", description="get item by id")
async def read_item(item_id: int):
    logger.info("getting an item!")
    return {"item_id": item_id}


@router.post("/items/", name="Upload Item", description="upload item")
async def create_item(item: Item):
    logger.info("posting an item!")

    return {"message": "Item created successfully"}
