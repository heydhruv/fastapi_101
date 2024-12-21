from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Order matters¶

# When creating path operations, you can find situations where you have a fixed path.

# Like / users/me, let's say that it's to get data about the current user.

# And then you can also have a path / users/{user_id} to get data about a specific user by some user ID.

# Because path operations are evaluated in order, you need to make sure that the path for / users/me is declared before the one for / users/{user_id}:



# Predefined values use Enum

class ModelName(str, Enum):
    darpa = "darpa"
    cia = "cia"
    nasa = "nasa"


@app.get("/models/{model_name}")
async def read_model(model_name: ModelName):
    if model_name == ModelName.darpa:
        return {"model_name": model_name, "details": "The Defense Advanced Research Projects Agency"}
    if model_name == ModelName.cia:
        return {"model_name": model_name, "details": "The Central Intelligence Agency"}
    if model_name == ModelName.nasa:
        return {"model_name": model_name, "details": "The National Aeronautics and Space Administration"}