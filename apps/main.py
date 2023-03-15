#!/usr/bin/python3
"""Entry point for the event planner."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from models.db_connect import db_conn
from routes import users, events

app: FastAPI = FastAPI()

# register origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


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
