import pytest
from fastapi import HTTPException, status
from app.dependencies import auth


class DummyDepends:
    def __init__(self, value):
        self.value = value
    def __call__(self, *args, **kwargs):
        return self.value


def test_get_current_user_valid_token(monkeypatch):
    """
    Test that get_current_user returns payload for a valid token.
    """
    payload = {"sub": "user_id"}
    monkeypatch.setattr(auth, "verify_token", lambda token: payload)
    result = auth.get_current_user(token="sometoken")
    assert result == payload


def test_get_current_user_invalid_token(monkeypatch):
    """
    Test that get_current_user raises HTTPException for invalid token.
    """
    monkeypatch.setattr(auth, "verify_token", lambda token: None)
    with pytest.raises(HTTPException) as exc:
        auth.get_current_user(token="badtoken")
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert "credentials" in exc.value.detail


def test_get_current_user_raises_on_exception(monkeypatch):
    """
    Test that get_current_user raises HTTPException if verify_token throws.
    """
    def raise_exc(token):
        raise Exception("fail")
    monkeypatch.setattr(auth, "verify_token", raise_exc)
    with pytest.raises(HTTPException) as exc:
        auth.get_current_user(token="anytoken")
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
