from fastapi import APIRouter
from src.main.model.policy import Policy

from src.main.util.logger import logger



router = APIRouter(tags=["Policy Manager"])


@router.post("/policies/", name="Get Policy", description="get policy by id")
async def retrieve_policyes() -> Policy:
    logger.info("getting a sample policy.")
    
    sample_policy = Policy(policy_id="abc123", name="hey", price=4.5)

    return sample_policy
    