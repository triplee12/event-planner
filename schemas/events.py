#!/usr/bin/python3
"""Event schemals for database models."""
from datetime import date, time
from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import (
    JSON, SQLModel, Field, Column,
    TIME, DATE, Relationship, String, ForeignKey
)


class Event(SQLModel, table=True):
    """
    Event schema for database models design.

    Args:
        id (int): unique identifier for an event
        title (str): title of the event
        image (str): image of the event
        description (str): description of the event
        tags (list): list of event tags
        start_date (Date): start date of the event
        start_time (Time): start time of the event
        end_date (Date): end date of the event
        location (str): location of the event

    """

    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    start_date: date = Field(sa_column=Column(DATE))
    start_time: time = Field(sa_column=Column(TIME(timezone=True)))
    end_date: date = Field(sa_column=Column(DATE))
    location: str
    creator: Optional[str] = Field(
        sa_column=Column(
            String,
            ForeignKey(
                "user.email",
                ondelete="CASCADE"
            ),
            nullable=False
        )
    )
    owner = Relationship(
        link_model="user",
        sa_relationship="user"
    )

    class Config:
        """Event schema configuration."""

        arbitrary_types_allowed: bool = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": """
                    We will be discussing the contents of the FastAPI book in
                    this event.
                    Ensure to come with your own copy to win gifts!
                """,
                "tags": ["python", "fastapi", "book", "launch"],
                "start_date": "2023-03-11",
                "start_time": "12:00:00",
                "end_date": "2023-03-11",
                "location": "Google Meet",
                "creator": "Me Yul"
            }
        }


class EventUpdate(SQLModel):
    """
    Event schema for database models design.

    Args:
        title Optional[str]: title of the event
        image Optional[str]: image of the event
        description Optional[str]: description of the event
        tags Optional[list]: list of event tags
        start_date Optional[Date]: start date of the event
        start_time Optional[Time]: start time of the event
        end_date Optional[Date]: end date of the event
        location Optional[str]: location of the event

    """

    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    start_date: Optional[date]
    start_time: Optional[time]
    end_date: Optional[date]
    location: Optional[str]
    creator: Optional[str]

    class Config:
        """Event schema configuration."""

        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": """
                    We will be discussing the contents of the FastAPI book in
                    this event.
                    Ensure to come with your own copy to win gifts!
                """,
                "tags": ["python", "fastapi", "book", "launch"],
                "start_date": "2023-03-11",
                "start_time": "12:00:00",
                "end_date": "2023-03-11",
                "location": "Google Meet",
                "creator": "Me Yul"
            }
        }


class EventRes(BaseModel):
    """
    Event response schema for database models design.

    Args:
        id (int): unique identifier for an event
        title (str): title of the event
        image (str): image of the event
        description (str): description of the event
        tags (list): list of event tags
        start_date (Date): start date of the event
        start_time (Time): start time of the event
        end_date (Date): end date of the event
        location (str): location of the event
        creator (str): the event creator

    """

    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    start_date: date
    start_time: time
    end_date: date
    location: str
    creator: str

    class Config:
        """Event schema configuration."""

        orm_mode: bool = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": """
                    We will be discussing the contents of the FastAPI book in
                    this event.
                    Ensure to come with your own copy to win gifts!
                """,
                "tags": ["python", "fastapi", "book", "launch"],
                "start_date": "2023-03-11",
                "start_time": "12:00:00",
                "end_date": "2023-03-11",
                "location": "Google Meet",
                "creator": "Me Yul"
            }
        }
