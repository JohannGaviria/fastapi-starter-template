from fastapi.testclient import TestClient
from app.main import app


def test_read_root():
    """
    Test that the root endpoint returns the welcome message.
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Starter Template"}


def test_cors_headers():
    """
    Test that CORS headers are present in the response (if allowed by config).
    """
    client = TestClient(app)
    response = client.get("/", headers={
        "Origin": "http://example.com"
    })
    # CORS header should be present if the origin is allowed
    cors_header = response.headers.get("access-control-allow-origin")
    allowed = ["*", "http://example.com"]
    if cors_header is not None:
        assert cors_header in allowed
    else:
        # If not present, at least CORS middleware is active (allow-credentials header)
        assert "access-control-allow-credentials" in response.headers
