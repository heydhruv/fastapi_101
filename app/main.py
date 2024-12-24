from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="the description of the item", max_length=300
    )
    price: float = Field(gt=0, description="must be a positive float")


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"message": "body fields"}
    return results
