from fastapi import APIRouter, HTTPException
from src.main.service.repository_service import RepositoryService
from src.main.model.vehicle import Vehicle

from src.main.util.logger import logger


router = APIRouter(tags=["Sample Controller"])

repository_service = RepositoryService()

@router.get("/mock-car", name="gets a mock car", description="car!")
async def get_mock_vehicle() -> Vehicle:

    logger.info("getting a mock car.")
    vehicle = Vehicle()
    return vehicle

@router.post("/car", name="saves a car", description="save car!")
async def save_vehicle(vehicle: Vehicle) -> Vehicle:

    logger.info("saving a car.")
    repository_service.save_vehicle(vehicle)
    return vehicle

@router.get("/car", name="gets a car", description="get car!")
async def get_vehicle(license_plate: str) -> Vehicle:

    logger.info("getting a car.")
    vehicle = repository_service.get_vehicle(license_plate)
    if vehicle is None:
        raise HTTPException(status_code=204, detail="Vehicle not found")
    return vehicle
    