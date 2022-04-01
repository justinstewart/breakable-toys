from fastapi.testclient import TestClient

from src.asgi import app


def test_hello_world():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
