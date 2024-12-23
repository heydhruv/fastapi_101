from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50) ]= None):
    response = {"message": "No q"}
    if q:
        return {"q": q}
    return response

# list / multiple values

# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = None): #q=foo&q=bar
#     query_items = {"q": q}
#     return query_items

# Alias
# Deprecated
