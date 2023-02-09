import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_PASS, DB_HOST, TEST_DB_NAME, DB_PORT, DB_USER

from database.models import Base
from app.main import app
from app.dependencies import get_db

TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{TEST_DB_NAME}"
engine_test = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine_test, autoflush=False)

Base.metadata.create_all(bind=engine_test)


async def prepare_databse():
    await Base.metadata.create_all(bind=engine_test)
    yield
    await Base.metadata.drop_all(bind=engine_test)


# @pytest.fixture(autouse=True, scope="session")
# def prepare_database():
#     with engine_test.begin() as conn:
#         conn.run_sync(Base.metadata.create_all(engine_test))
#     yield
#     # with engine_test.begin() as conn:
#     #     conn.run_sync(Base.metadata.drop_all(engine_test))
# prepare_database()

# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# app.dependency_overrides[get_db] = override_get_db
#
# client = TestClient(app)
#
# def test_register_user():
#     response = client.post("/auth/register",
#                            json={"email": "test_email@com.com", "username": "test_username", "password": "test_password"})
#     assert response.status_code == 200, response.text
#     data = response.json()
