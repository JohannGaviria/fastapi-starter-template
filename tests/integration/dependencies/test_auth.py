from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from fastapi import Depends
from app.dependencies.auth import get_current_user
from app.core.jwt import create_access_token


app = FastAPI()


@app.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    return {"user": user}


def test_protected_route_valid_token():
    """
    Test access protected route with valid token returns 200 and user payload.
    """
    payload = {"sub": "user_id"}
    token = create_access_token(payload)
    client = TestClient(app)
    response = client.get("/protected", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["user"]["sub"] == "user_id"


def test_protected_route_invalid_token():
    """
    Test access protected route with invalid token returns 401.
    """
    client = TestClient(app)
    response = client.get("/protected", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "credentials" in response.json()["detail"].lower()
