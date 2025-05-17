from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from app.core.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.

    Args:
        data (dict): The data to encode in the token (payload).
        expires_delta (Optional[timedelta]): Optional expiration time delta.

    Returns:
        str: Encoded JWT as a string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    if isinstance(encoded_jwt, bytes):
        encoded_jwt = encoded_jwt.decode('utf-8')
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    """
    Verify and decode a JWT access token.

    Args:
        token (str): The JWT token to verify.

    Returns:
        Optional[dict]: Decoded payload if valid, None if invalid or expired.
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except (ExpiredSignatureError, InvalidTokenError):
        return None
