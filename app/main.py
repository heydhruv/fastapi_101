from fastapi import FastAPI

app = FastAPI()

response = [{"item_name":"Foo"}, {"item_name":"bar"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, q: str | None = None, short: bool = False):     # q is optional    short is bool typecast
    if q:
        return {"q": q}
    if not short:
        {"message": "Bool is not"}
    return response[skip : skip + limit]

# parameters without any default values or optional None are not required
# multi path and query parameters

@app.get("/users/{user_id}/items/{item_name}")
async def read_user_items(user_id: int, item_id: int, q: str | None = None, short: bool = False):
    if q:
        return {"q": q}
    if not short:
        {"message": "Bool is not"}
    return response[{"message": "200"}]
