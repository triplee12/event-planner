#!/usr/bin/python3
"""JWT handler for authentication requests."""
from datetime import datetime
from time import time
from fastapi import HTTPException, status
from jose import jwt, JWTError
from event_planner.models.db_connect import settings


def create_access_token(user: str) -> str:
    """Create a new access token."""
    payload = {
        "user": user,
        "expires": time() + 3600
    }

    token = jwt.encode(
        payload, key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return token


def verify_token(token: str):
    """Verify access token."""
    try:
        data = jwt.decode(
            token, key=settings.SECRET_KEY,
            algorithms=settings.ALGORITHM
        )
        expire = data.get('expires')

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied."
            )

        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access token has expired!"
            )
        return data
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid access token."
        ) from exc
