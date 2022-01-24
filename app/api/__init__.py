"""
API
"""
from fastapi import APIRouter

from app.api.v1.hello import hello_router

# ROUTER
router = APIRouter()
router.include_router(hello_router,
                      prefix="/v1/hello",
                      # dependencies=[Depends(validate_request)]
                      )
