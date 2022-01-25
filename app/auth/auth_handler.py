"""
Auth Handler
"""
import time
from typing import Dict

import jwt
from app.core import settings

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = settings.ALGORITHM


def token_response(token: str):
    """
    Token Response
    """
    return {
        "access_token": token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    """
    Sign JWT
    """
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    """
    Decode JWT
    """
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        return {'error': e.args}
