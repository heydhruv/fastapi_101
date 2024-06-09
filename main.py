from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def Home() :
    return {"Hello": "world"}


@app.get("/about")
def About() -> str :
    return "Amazing Company"
