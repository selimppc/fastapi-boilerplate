"""
POSTS
"""
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.models.post import PostSchema

posts_router = APIRouter()

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]


@posts_router.get("/", tags=["posts"])
async def get_posts() -> dict:
    """
    list of posts
    """
    return {"data": posts}


@posts_router.get("/{id}", tags=["posts"])
async def get_single_post(id: int) -> JSONResponse:
    """ get a single post """
    if id > len(posts):
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    for post in posts:
        if post["id"] != id:
            continue
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=post
        )
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


@posts_router.post("/", tags=["posts"])
async def add_post(post: PostSchema) -> JSONResponse:
    post.id = len(posts) + 1
    posts.append(post.dict())

    return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
