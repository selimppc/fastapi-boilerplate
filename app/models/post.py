from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    """
    Post Schema
    """
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        """
        config extra
        """
        schema_extra = {
            "example" : {
                "title" : "Securing fastapi",
                "description" : " description goes well."
            }

        }
