#!/usr/bin/python3
"""Events routes."""
from typing import List
from fastapi import (
    APIRouter, Depends,
    HTTPException,
    status
)
from sqlmodel import select
from auths.authenticate import authenticate
from models.db_connect import get_session
from schemas.events import Event, EventRes, EventUpdate

event_router: APIRouter = APIRouter(prefix="/events", tags=["Events"])


@event_router.get("/", response_model=List[EventRes])
async def get_events(session=Depends(get_session)) -> List[EventRes]:
    """Return all the available events."""
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{event_id}", response_model=Event)
async def get_an_event(
    event_id: int, user: str = Depends(authenticate),
    session=Depends(get_session)
) -> Event:
    """Return an event by id."""
    event = session.get(Event, event_id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
    )


@event_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_event(
    event: Event, user: str = Depends(authenticate),
    session=Depends(get_session)
) -> dict:
    """Create a new event."""
    event.creator = user["user"]
    session.add(event)
    session.commit()
    session.refresh(event)
    return {"message": "Event created successfully."}


@event_router.delete(
    "/delete/{event_id}",
    # status_code=status.HTTP_204_NO_CONTENT
)
async def delete_an_event(
    event_id: int, user: str = Depends(authenticate),
    session=Depends(get_session)
):
    """Delete an event."""
    event = session.get(Event, event_id)
    if event and user["user"] == event.creator:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}

    if event and user["user"] != event.creator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied!"
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
    )


@event_router.put(
    "/edit/{event_id}",
    status_code=status.HTTP_201_CREATED
)
async def update_event(
    event_id: int,
    new_data: EventUpdate,
    user: str = Depends(authenticate),
    session=Depends(get_session)
) -> dict:
    """Update an events."""
    event = session.get(Event, event_id)

    if event and user["user"] == event.creator:
        event_data = new_data.dict(exclude_unset=True)
        for k, v in event_data.items():
            setattr(event, k, v)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    if event and user["user"] != event.creator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied!"
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
    )
