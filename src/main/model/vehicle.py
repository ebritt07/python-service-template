from pydantic import BaseModel, Field

from src.main.model.enum import Transmission

class Vehicle(BaseModel):
    licensePlate: str = "7GRS30"
    transmission: Transmission = Transmission.AUTOMATIC
    mpgHighway: int = 45
    mpgCity: int = 30
    make: str = "Ford"
    model: str = "Fusion Hybrid"