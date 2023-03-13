#!/usr/bin/python3
"""Password hasher module."""
from passlib.context import CryptContext

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    """Hash user's plain password.

    Return the hashed password and verify the password when user try to login.
    """

    def create_hash(self, password: str) -> str:
        """Create hash version of the password and return it."""
        return pwd_context.hash(password)

    def verify_hash(self, password: str, hashed_pwd: str) -> bool:
        """Verify hashed password."""
        return pwd_context.verify(password, hashed_pwd)
