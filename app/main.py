from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post('/login/')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


# Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.
