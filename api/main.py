from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .router import items, user

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(user.router)
app.include_router(items.router)


@app.get('/')
async def root():
    return {'message': 'Welcome to the FastAPI 101 API!'}
