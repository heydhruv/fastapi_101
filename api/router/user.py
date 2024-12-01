from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Dhruv"}, {"username": "Jay"}]


@router.get("users/me", tags=["users"])
async def read_current_user():
    return {"username": "Dhruv"}


@router.get("users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
