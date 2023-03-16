"""Test for events module."""
import httpx
import pytest
import pytest_asyncio
from event_planner.auths.jwt_handler import create_access_token


@pytest_asyncio.fixture(scope="module")
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
async def test_unauth_user_create_event(
    test_client: httpx.AsyncClient
) -> None:
    """Test for unauthenticated user to create event."""
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
        "Content-Type": "application/json"
    }
    test_response = {
        "detail": "Not authenticated"
    }
    response = await test_client.post(
        "/events/create",
        json=payload, headers=headers
    )

    assert response.status_code == 401
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


@pytest.mark.asyncio
async def test_not_authenticated_user_get_event(
    test_client: httpx.AsyncClient
) -> None:
    """Test for not authenticated user to retrieve an event."""
    headers = {
        "Content-Type": "application/json"
    }
    response = await test_client.get(
        "/events/1", headers=headers, follow_redirects=True
    )
    test_response = {
        "detail": "Not authenticated"
    }

    assert response.status_code == 401
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_update(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Test for event update."""
    payload = {
        "title": "Update From Test Update",
        "tags": ["Update tag",]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {create_token}"
    }
    response = await test_client.put(
        "/events/edit/1", json=payload,
        headers=headers, follow_redirects=True
    )

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


@pytest.mark.asyncio
async def test_not_exist_event_update(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Test for not existing event update."""
    payload = {
        "title": "Not Update From Test Update",
        "tags": ["Not Update tag",]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {create_token}"
    }
    response = await test_client.put(
        "/events/edit/2", json=payload,
        headers=headers, follow_redirects=True
    )
    res_message = {"detail": "Event not found"}

    assert response.status_code == 404
    assert response.json() == res_message


@pytest.mark.asyncio
async def test_not_athenticate_user_update_event(
    test_client: httpx.AsyncClient
) -> None:
    """Test for not authenticated user update an event."""
    payload = {
        "title": "Update From Test Update",
        "tags": ["Update tag",]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = await test_client.put(
        "/events/edit/1", json=payload,
        headers=headers, follow_redirects=True
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_event(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Test for event delete."""
    headers = {
        "Authorization": f"Bearer {create_token}"
    }
    response = await test_client.delete(
        "events/delete/1", headers=headers, follow_redirects=True
    )
    res_message = {"message": "Event deleted successfully"}

    assert response.status_code == 200
    assert response.json() == res_message


@pytest.mark.asyncio
async def test_delete_not_exist_event(
    test_client: httpx.AsyncClient,
    create_token: str
) -> None:
    """Test for deleting not exist event."""
    headers = {
        "Authorization": f"Bearer {create_token}"
    }
    response = await test_client.delete(
        "events/delete/2", headers=headers, follow_redirects=True
    )
    res_message = {"detail": "Event not found"}

    assert response.status_code == 404
    assert response.json() == res_message


@pytest.mark.asyncio
async def test_not_authenticate_user_delete_event(
    test_client: httpx.AsyncClient
) -> None:
    """Test for not authenticated user delete an event."""
    response = await test_client.delete(
        "events/delete/1", follow_redirects=True
    )
    res_message = {"detail": "Not authenticated"}

    assert response.status_code == 401
    assert response.json() == res_message
