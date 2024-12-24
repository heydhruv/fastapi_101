from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.post("/items/")
async def read_items(filter_query: FilterParams):
    return filter_query
