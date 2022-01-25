"""
API
"""
from fastapi import APIRouter

from app.api.v1.hello import hello_router
from app.api.v1.posts import posts_router
from app.api.v1.users import users_router

# ROUTER
router = APIRouter()
router.include_router(hello_router,
                      prefix="/v1/hello",
                      # dependencies=[Depends(validate_request)]
                      )
router.include_router(posts_router,
                      prefix="/v1/posts"
                      # dependencies=[]
                      )
router.include_router(users_router,
                      prefix="/v1/users")
