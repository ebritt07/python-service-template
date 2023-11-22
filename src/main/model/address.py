
from pydantic import BaseModel


class Address(BaseModel):
    
    addressLine1: str = "123 Cherry Lane"
    addressLine2: str = "Apt 2"
    city: str = "Atlanta"
    state: str = "Georgia"
    postalCode: str = "30318"
    country: str = "USA"
