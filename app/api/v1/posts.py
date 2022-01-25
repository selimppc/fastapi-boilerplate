"""
posts crud operation
"""
from typing import List
from fastapi import APIRouter, status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from app.core import settings
from app.models.post import PostSchema, UpdatePostSchema
import motor.motor_asyncio

posts_router = APIRouter()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
db = client.college


@posts_router.get(
    "/", tags=["posts"],
    response_description="List of posts",
    response_model=List[PostSchema]
)
async def list_posts() -> dict:
    """
    list of posts
    """
    posts_data = await db["posts"].find().to_list(2)
    return posts_data


@posts_router.post(
    "/",
    tags=["posts"],
    response_description="create new post ",
    response_model=PostSchema
)
async def create_post(post: PostSchema = Body(...)) -> JSONResponse:
    """
    create new post
    """
    post = jsonable_encoder(post)
    new_post = await db["posts"].insert_one(post)
    created_post = await db["posts"].find_one({"_id": new_post.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_post)


@posts_router.get(
    "/{id}",
    tags=["posts"],
    response_description=" get a single post",
    response_model=PostSchema
)
async def get_single_post(id: int) -> dict:
    """
    get a single post
    """
    if (post := await db["posts"].find_one({"_id": id})) is not None:
        return post
    raise HTTPException(status_code=404, detail=f"Post {id} not found")


@posts_router.put(
    "/{id}",
    response_description="update a post",
    response_model=PostSchema
)
async def update_post(id: str, post: UpdatePostSchema = Body(...)) -> dict:
    """
    updated a post
    """
    post = {k: v for k, v in post.dict().items() if v is not None}
    if len(post) >= 1:
        update_result = await db["posts"].update_one({"_id": id}, {"$set": post})
        if update_result.modified_count == 1:
            if (
                updated_post := await db["posts"].find_one({"_id": id})
            ) is not None:
                return updated_post
    if (existing_post := await db["posts"].find_one({"_id": id})) is not None:
        return existing_post

    raise HTTPException(status_code=404, detail=f"Post {id} not found")


@posts_router.delete(
    "/{id}",
    tags=["posts"],
    response_description="delete a post"
)
async def delete_post(id: str) -> JSONResponse:
    delete_result = await db["posts"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Post {id} not found")