"""
POST Schema
"""

from bson import ObjectId
from pydantic import BaseModel, Field
from app.models._id_object import PyObjectId


class PostSchema(BaseModel):
    """
    Post Schema
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        """
        config extra
        """
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Securing fastApi",
                "description": " description goes well."
            }

        }


class UpdatePostSchema(BaseModel):
    """
    Post Schema
    """
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        """
        config extra
        """
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Securing fastApi",
                "description": " description goes well."
            }
        }
