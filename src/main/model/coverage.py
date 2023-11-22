
from pydantic import BaseModel


class CoverageDTO(BaseModel):
    code: str = "COMP"
    label: str = "Comprehensive"
    deductible: float = 100
    code: str = "abc123"
    limitPerAccident: float = 500000