"""
FastAPI v0
"""
from fastapi import FastAPI

from starlette.responses import Response

from app.core.settings import default_route_str
from app.api import router as endpoint_router
from app.db.mongodb import close, connect

import uvicorn


app = FastAPI(title="FastAPI", version="0")
app.include_router(endpoint_router, prefix=default_route_str)


@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts
    """
    await connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown
    """
    await close()


@app.get("/")
async def home():
    """Home page
    """
    return Response("FastAPI V0")


if __name__ == "__main__":
    uvicorn.run(app, log_level="debug", reload=True)
