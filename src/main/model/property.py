from typing import Optional
from pydantic import BaseModel


class PropertyDataDTO(BaseModel):
    bodyStyle: str = "4DR"
    vin: str = "2NM3E123D37398562"
    model: str = "Model 3"
    year: int = 2019
    make: str = "Tesla"

class PropertyDTO(BaseModel):
      type: str = "vehicle"
      data: Optional[PropertyDataDTO] = PropertyDataDTO()