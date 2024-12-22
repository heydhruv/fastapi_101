from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/item")
async def item(item: Item):
    if item.tax:
        return {"response": "i know man Nirmala tai is a headache"}
    if item.price > 1000000:
        return {"response": "Expensive Stuff Bro"}
    return item

# Request body + path + query parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    return {"item_id": item_id, **item.model_dump()}
