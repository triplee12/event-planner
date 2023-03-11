#!/usr/bin/python3
"""Entry point for the event planner."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from models.db_connect import db_conn
from routes import users, events

app: FastAPI = FastAPI()


@app.on_event("startup")
def on_startup():
    """Connect to database on app startup."""
    db_conn()


@app.get("/")
async def main() -> dict:
    """Entry point for all routes."""
    return RedirectResponse(url="/events")


app.include_router(users.user_router)
app.include_router(events.event_router)
