#!/usr/bin/python3
"""Pytest fixture module config."""
import asyncio
import httpx
import pytest_asyncio
from sqlmodel import SQLModel
from event_planner.models.db_connect import db_conn, get_session, engine_url
from event_planner.apps.main import app


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Event loop for the test cases."""
    loop = asyncio.new_event_loop()
    asyncio.get_event_loop_policy().set_event_loop(loop)
    asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


db_conn()
get_session()


@pytest_asyncio.fixture(scope="session")
async def test_client():
    """Create a default test client."""
    async with httpx.AsyncClient(
        app=app,
        base_url="http://127.0.0.1:8000"
    ) as client:
        yield client
        SQLModel.metadata.drop_all(
            bind=engine_url
        )
