#!/usr/bin/python3
"""Event schemals for database models."""
from datetime import datetime
from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    """
    Event schema for database models design.

    Args:
        id (int): unique identifier for an event
        title (str): title of the event
        image (str): image of the event
        description (str): description of the event
        tags (list): list of event tags
        start_date (str): start date of the event
        end_date (str): end date of the event
        location (str): location of the event

    """

    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    start_date: datetime
    end_date: datetime
    location: str

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
                "start_date": "2023-03-11:T12:00:00",
                "end_date": "2023-03-11:T12:00:00",
                "location": "Google Meet"
            }
        }
