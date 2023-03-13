#!/usr/bin/python3
"""JWT handler for authentication requests."""
import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError
