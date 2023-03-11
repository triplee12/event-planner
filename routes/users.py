#!/usr/bin/python3
"""User routes."""
from fastapi import APIRouter, HTTPException, status
from schemas.users import User, UserSignIn

user_router: APIRouter = APIRouter(prefix="/users", tags=["Users"])
users = {}


@user_router.post("/signup")
async def signup(data: User) -> dict:
    """User sign up route."""
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email already exists."
        )
    users[data.email] = data.dict()
    return {"message": "User successfully registered."}


@user_router.post("/login")
async def login(user: UserSignIn) -> dict:
    """User login route."""
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist."
        )

    if users[user.email]["password"] != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    return {"message": "Signed in successfully"}
