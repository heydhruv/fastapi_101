from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


class BaseUser(BaseModel):
    username: str
    full_name: str | None = None

@app.post("/items/", response_model=Item)
async def create_item(item: BaseUser) -> Any:
    return item

# response_model has higher precedence then return type

# Other Return Type Annotations
# from fastapi.responses import JSONResponse, RedirectResponse
# app.get("/portal")


# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# this will fail Response | dict:
# so you can do this response_model=None

# response_model_exclude_defaults=True


