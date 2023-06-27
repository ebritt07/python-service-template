from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Python Service", description="sample py backend")


class Item(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}", name="Get Item", description="get item by id", tags=["Item controller"])
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/", name="Upload Item", description="upload item", tags=["Item controller"])
async def create_item(item: Item):
    # Process the item data, e.g., save to a database
    return {"message": "Item created successfully"}
