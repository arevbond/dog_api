from app.main import app
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user(prepare_database):
    response = client.post("/auth/register", json={
        "email": "user_test3@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "test_user3"
    })
    assert response.status_code == 201, response.text
    data = response.json()
