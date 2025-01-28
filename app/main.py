from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None
    tags: set[str] = set()


@app.post('/items/', response_model=Item, tags=[Tags.items], status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
