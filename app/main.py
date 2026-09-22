from fastapi import FastAPI

from app.service import build_message

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/hello/{name}")
async def hello(name: str):
    message = build_message(name)
    return {
        "success": True,
        "message": message
    }