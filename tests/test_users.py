#!/usr/bin/python3
"""Test module for users."""
import httpx
import pytest


@pytest.mark.asyncio
async def test_user_sign_up(test_client: httpx.AsyncClient) -> None:
    """Test for new user sign up."""
    payload: dict[str, str] = {
        "email": "tiplee@gmail.com",
        "first_name": "Ebuka",
        "last_name": "Ejie",
        "password": "password00ps",
        "date_of_birth": "2023-03-11"
    }

    headers: dict[str, str] = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    test_res = {
        "message": "Signed up successfully"
    }
    response = await test_client.post(
        "/users/signup",
        json=payload, headers=headers
    )

    assert response.status_code == 201
    assert response.json() == test_res
