from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 0.08
    tags: list[str] = []


items = {
    "foo": {"name": "foo", "price": "10"},
    "bar": {"name": "bar", "price": "12", "tax": 0.01, "description": "BARZZZZZZZ"},
    "foz": {"name": "foz", "price": "40", "description": "FOZZZZZZZZZ", "tax": 0.1}
}


@app.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: str, item_data: Item):
    update_item_encoded = jsonable_encoder(item_data)
    items[item_id] = update_item_encoded
    return update_item_encoded
