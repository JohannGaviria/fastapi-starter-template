from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.jwt import verify_token


# OAuth2 scheme for extracting bearer token from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependency to get the current user from a JWT token.
    Verifies the token and returns the payload if valid.
    Raises HTTP 401 if credentials are invalid or missing.

    Args:
        token (str): JWT token extracted from the request.

    Returns:
        dict: Decoded JWT payload representing the user.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="The credentials could not be validated.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        if payload is None:
            raise credentials_exception
        return payload
    except Exception:
        raise credentials_exception
