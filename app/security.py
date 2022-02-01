""" security """
import base64
from dataclasses import dataclass
from functools import lru_cache

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from starlette import status

from app.config import settings


@dataclass
class AuthUser:
    """ Auth user or consumer """
    username: str
    platform_id: str
    client_id: str
    user_type: str = 'anonymous'


bearer_authorization = HTTPBearer(
    scheme_name='Authorization'
)


async def validate_auth_token(http_authorization_credentials=Depends(bearer_authorization)):
    """ consumer token authorization """
    try:
        payload = decode_auth_token(token=http_authorization_credentials.credentials)
        user = AuthUser(username=payload['username'],
                        platform_id=payload['platform_id'],
                        client_id=payload['client_id'],
                        user_type=payload['user_type'])
        return user
    except(jwt.InvalidSignatureError, jwt.ExpiredSignatureError, jwt.DecodeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid_token",
        )


@lru_cache()
def get_public_key(key):
    """ get public key """
    base64_decoded_key = base64.b64decode(key)
    bytes_key = bytes(base64_decoded_key)
    public_key = load_pem_public_key(bytes_key, backend=default_backend())
    return public_key


def decode_auth_token(token):
    """ decode auth (heimdall) token """
    public_key = get_public_key(key=settings.AUTH_PUBLIC_KEY)
    token_payload = jwt.decode(token, public_key, algorithm='RS256')
    return token_payload
