from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

items = {"foo": "the bar"}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found",
                            headers={"X-Error": "There goes my error"},)
    return items[item_id]


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exe: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f'Oops! {
            exe.name} did something.there goes rainbow!'}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"errors": exc.errors()})

@app.get('/unicorn/{name}')
async def read_unicorn(name: str):
    if name.lower() == 'rainbow':
        raise UnicornException('Rainbow')
    return {"unicorn_name": name}


@app.get("/items/{id}")
async def read_itemm(id: int):
    if id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": id}
