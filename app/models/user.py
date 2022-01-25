"""
User Model
"""

from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        def __init__(self):
            pass

        schema_extra = {
            "example": {
                "fullname": "Selim Reza",
                "email": "selim@reza.com",
                "password": "123456"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        def __init__(self):
            pass

        schema_extra = {
            "example": {
                "email": "selim@reza.com",
                "password": "123456"
            }
        }