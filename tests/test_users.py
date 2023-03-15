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


@pytest.mark.asyncio
async def test_login(test_client: httpx.AsyncClient):
    """Test for user login."""
    payload = {
        "username": "tiplee@gmail.com",
        "password": "password00ps"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await test_client.post(
        "/users/login",
        data=payload, headers=headers
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"


@pytest.mark.asyncio
async def test_get_all_users(test_client: httpx.AsyncClient) -> None:
    """Test for retrieving all users."""
    headers: dict[str, str] = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = await test_client.get(
        "/users", headers=headers, follow_redirects=True
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get__user(test_client: httpx.AsyncClient) -> None:
    """Test for retrieving a user by email."""
    headers: dict[str, str] = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = await test_client.get(
        "/users", headers=headers, follow_redirects=True,
        params="tiplee@gmail.com"
    )

    assert response.status_code == 200
