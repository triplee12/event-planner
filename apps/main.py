#!/usr/bin/python3
"""Entry point for the event planner."""
from fastapi import FastAPI
from routes import users, events

app: FastAPI = FastAPI()


@app.get("/")
async def main() -> dict:
    """Entry point for all routes."""
    return {"message": "Welcome to OpenEvent"}


app.include_router(users.user_router)
app.include_router(events.event_router)
