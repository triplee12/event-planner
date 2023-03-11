#!/usr/bin/python3
"""Database connection configurations."""
from sqlmodel import SQLModel, create_engine, Session
from schemas.events import Event

database_file: str = "planner.db"
database_connection_string: str = f"sqlite:///{database_file}"
connect_args: dict[str, bool] = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string, echo=True,
    connect_args=connect_args
)


def db_conn():
    """Make connection to database."""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """Get database session."""
    with Session(engine_url) as session:
        yield session
