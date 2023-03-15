#!/usr/bin/python3
"""Authenticate module for user authentication."""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwt_handler import verify_token

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    """Authenticate user using OAuth2 credentials."""
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access token."
        )
    decoded_token = verify_token(token)
    return decoded_token
