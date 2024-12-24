from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="ID of the item", gt=0)],
        size: Annotated[float, Query(ge=38, decimal_places=1)]
):
    return {"item_id": item_id, "size": size}
