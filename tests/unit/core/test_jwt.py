from datetime import timedelta
from app.core import jwt as jwt_module
from app.core.config import settings
import jwt as pyjwt


def test_create_access_token_returns_valid_jwt():
    """
    Test that create_access_token returns a valid
    JWT string and the payload contains the expected data and expiration.
    """
    data = {"sub": "user_id"}
    token = jwt_module.create_access_token(data)
    assert isinstance(token, str)
    payload = pyjwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    assert payload["sub"] == "user_id"
    assert "exp" in payload


def test_verify_token_valid():
    """
    Test that verify_token returns the correct payload for a valid token.
    """
    data = {"sub": "user_id"}
    token = jwt_module.create_access_token(data)
    payload = jwt_module.verify_token(token)
    assert payload is not None
    assert payload["sub"] == "user_id"


def test_verify_token_expired():
    """
    Test that verify_token returns None for an expired token.
    """
    data = {"sub": "user_id"}
    token = jwt_module.create_access_token(data, expires_delta=timedelta(seconds=-1))
    payload = jwt_module.verify_token(token)
    assert payload is None


def test_verify_token_invalid():
    """
    Test that verify_token returns None for an invalid token string.
    """
    invalid_token = "invalid.token.value"
    payload = jwt_module.verify_token(invalid_token)
    assert payload is None
