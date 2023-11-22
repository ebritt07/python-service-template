from typing import List
from fastapi import APIRouter
from src.main.model.coverage import CoverageDTO
from src.main.model.property import PropertyDTO
from src.main.model.address import Address
from src.main.model.policy import Policy

from src.main.util.logger import logger



router = APIRouter(tags=["Policy Manager"])


@router.post("/policies/", name="Get Policy", description="get policy by id")
async def retrieve_policyes() -> Policy:
    logger.info("getting a sample policy.")
    
    sample_policy = Policy()


    address: Address = Address()
    properties: List[PropertyDTO] = []

    properties.append(PropertyDTO(type="boat"))
    properties.append(PropertyDTO(type="other"))

    coverages: List[CoverageDTO] = []
    coverages.append(CoverageDTO(label="partial"))
    coverages.append(CoverageDTO(deductible=100))

    sample_policy.address = address
    sample_policy.properties = properties
    sample_policy.coverages = coverages

    return sample_policy
    