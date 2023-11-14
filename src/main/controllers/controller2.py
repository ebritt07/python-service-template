from fastapi import APIRouter
from pydantic import BaseModel

from src.main.util.logger import logger


class Car(BaseModel):
    make: str
    model: str
    price: float
    for_sale: bool


router = APIRouter(tags=["Controller 2"])


@router.get("/cars/{car_id}", name="Get Car", description="get car by id")
async def read_car(car_id: int):
    logger.info("getting an car!")
    return {"car_id": car_id}


@router.post("/cars/", name="Upload Car", description="upload car")
async def create_car(car: Car):
    logger.info("posting an car!")
    return {"message": "Car created successfully"}
