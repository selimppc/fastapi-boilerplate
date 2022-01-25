"""
Hello World
"""
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

hello_router = APIRouter()


@hello_router.get("/")
async def home():
    hello_world = "Hello World"

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=hello_world
    )
