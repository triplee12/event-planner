"""Test for events module."""
import httpx
import pytest
from event_planner.auths.jwt_handler import create_access_token


@pytest.fixture(scope="module")
async def create_token() -> str:
    """Create access token for test_client."""
    return create_access_token("tiplee@gmail.com")


@pytest.mark.asyncio
async def test_create_event(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Create mock event."""
    payload = {
        "creator": "testuser@packt.com",
        "title": "FastAPI Book Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": """We will be discussing the contents of
        the FastAPI book in this event.Ensure to come with
        your own copy to win gifts!""",
        "tags": ["python", "fastapi", "book", "launch"],
        "location": "Google Meet",
        "start_date": "2023-03-16",
        "start_time": "07:00:00",
        "end_date": "2023-07-02"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {create_token}"
    }
    test_response = {
        "message": "Event created successfully."
    }
    response = await test_client.post(
        "/events/create",
        json=payload, headers=headers
    )

    assert response.status_code == 201
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_get_events(
    test_client: httpx.AsyncClient
) -> None:
    """Test retrieve all events."""
    response = await test_client.get("/events", follow_redirects=True)

    assert response.status_code == 200
    assert response.json()[0]["id"] == 1


@pytest.mark.asyncio
async def test_get_event(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Test retrieve an event."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {create_token}"
    }
    response = await test_client.get(
        "/events/1", headers=headers, follow_redirects=True
    )

    assert response.status_code == 200
