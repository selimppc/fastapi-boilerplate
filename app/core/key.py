"""
Api Key validation
"""
from typing import Optional

from fastapi.security.api_key import APIKeyHeader
from fastapi import HTTPException, Security, Depends
# from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN

# from app.core.security import verify_key
from app.db.mongodb import AsyncIOMotorClient, get_database
from pydantic import EmailStr

api_key_scheme = APIKeyHeader(name="X-API-KEY", auto_error=False)
email_scheme = APIKeyHeader(name="X-EMAIL-ID", auto_error=False)


async def validate_request(
        api_key: Optional[str] = Security(api_key_scheme),
        email_id: Optional[EmailStr] = Security(email_scheme),
        db: AsyncIOMotorClient = Depends(get_database)
):
    """
    Validate a request with given email and api key
    to any endpoint resource
    """
    pass
