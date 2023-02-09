from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# def test_get_image():
#     response = client.get("/api/breeds/image/random/")
#     assert response.status_code == 200
#     # assert response.


# def test_get_home_page():
#     pass
