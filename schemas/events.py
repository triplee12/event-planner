#!/usr/bin/python3
"""Event schemals for database models."""
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
        location (str): location of the event

    """

    id: int
    title: str
    image: str
    description: str
    tags: List[str]
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
                "location": "Google Meet"
            }
        }
