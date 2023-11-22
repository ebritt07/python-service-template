from typing import List, Optional
from pydantic import BaseModel, Field
from src.main.model.property import PropertyDTO
from src.main.model.coverage import CoverageDTO
from src.main.model.address import Address

from src.main.model.enum import PolicyType

class Policy(BaseModel):
    policy_id: str = "abc123"
    type: PolicyType = PolicyType.AUTO
    carrier: Optional[str] = None
    policyNumber: str = "123-4678-C10-34Q"
    isActive: bool = False
    effectiveDate: str = "2022-06-10T00:00:00.000Z"
    expirationDate: str = "2022-06-10T00:00:00.000Z"
    address: Optional[Address] = None
    coverages: Optional[List[CoverageDTO]] = []
    properties: Optional[List[PropertyDTO]] = []