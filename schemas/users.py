#!/usr/bin/python3
"""User schema for the user database design."""
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .events import Event


class User(BaseModel):
    """User schema for the user database design.

    Args:
        email (EmailStr): valid email address of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
        password (str): password of the user
        events (Optional[list]): list of events that the user created
    """

    email: EmailStr
    first_name: str
    last_name: str
    password: str
    events: Optional[List[Event]]

    class Config:
        """User schema configuration."""

        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    """UserSignIn schema for the user login.

    Args:
        email (EmailStr): valid email address of the user
        password (str): password of the user
    """

    email: EmailStr
    password: str

    class Config:
        """User schema configuration for login."""

        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!"
            }
        }
