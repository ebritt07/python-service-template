
from pydantic import BaseModel

class Policy(BaseModel):
    policy_id: str
    name: str
    price: float