#!/usr/bin/python3
"""Events routes."""
from typing import List
from fastapi import APIRouter, Body, HTTPException, status
from schemas.events import Event

event_router: APIRouter = APIRouter(prefix="/events", tags=["Events"])
events: list = []


@event_router.get("/", response_model=List[Event])
async def get_events() -> List[Event]:
    """Return all the available events."""
    return events


@event_router.get("/{event_id}", response_model=Event)
async def get_an_event(event_id: int) -> Event:
    """Return an event by id."""
    for event in events:
        if event["id"] == event_id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
    )


@event_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_event(event: Event = Body(...)) -> dict:
    """Create a new event."""
    events.append(event.dict())
    return {"message": "Event created successfully."}


@event_router.delete(
    "/delete/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_an_event(event_id: int):
    """Delete an event."""
    for event in events:
        if event["id"] == event_id:
            events.remove(event)
            # return {"message": "Event deleted successfully"}
    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail="Event not found"
    # )


@event_router.delete("/all/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all():
    """Delete all events."""
    events.clear()
    # return {"message": "Events deleted successfully"}
