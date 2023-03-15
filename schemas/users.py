#!/usr/bin/python3
"""User schema for the user database design."""
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql import func
from sqlmodel import SQLModel, Field, Column, DateTime, Date, String


class User(SQLModel, table=True):
    """User schema for the user database design.

    Args:
        email (EmailStr): valid email address of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
        password (str): password of the user
        date_of_birth (date): birth date of the user
    """

    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(
        sa_column=Column(String, unique=True, nullable=False)
    )
    first_name: str
    last_name: str
    password: str
    date_of_birth: date = Field(sa_column=Column(Date))
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now()
        )
    )

    class Config:
        """User schema configuration."""

        arbitrary_types_allowed: bool = True
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "strong!!!",
                "date_of_birth": "2013-07-01"
            }
        }


class TokenResponse(BaseModel):
    """TokenResponse schema for the user login.

    Args:
        access_token (str): valid email address of the user
        token_type (str): password of the user
    """

    access_token: str
    token_type: str

    class Config:
        """User schema configuration for login."""

        schema_extra = {
            "example": {
                "access_token": "f234a456s67899t9ap544i8",
                "token_type": "Bearer"
            }
        }


class UserRes(BaseModel):
    """UserRes response schema for the user database design.

    Args:
        id (int): unique indentifier
        email (EmailStr): valid email address of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
        date_of_birth (date): birth date of the user
    """

    id: int
    email: str
    first_name: str
    last_name: str
    date_of_birth: date

    class Config:
        """User response config."""

        orm_mode: bool = True
