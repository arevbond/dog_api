# import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
# from httpx import AsyncClient
from app.dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Base
from app.auth.db import get_async_session

from config import DB_PASS, DB_HOST, TEST_DB_NAME, DB_PORT, DB_USER
from app.main import app

# DATABASE
TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{TEST_DB_NAME}"

engine_test = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine_test, autoflush=False, class_=AsyncSession, expire_on_commit=False)


# TEST_SQLALCHEMY_DATABASE_URL = f"postgresql:asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{TEST_DB_NAME}"
# engine_test = create_async_engine(TEST_SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
# async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
#
# Base.metadata.bind = engine_test


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


app.dependency_overrides[get_async_session] = override_get_db


@pytest.fixture()
def prepare_database():
    Base.metadata.create_all(engine_test)
    yield
    Base.metadata.drop_all(engine_test)


# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     async with engine_test.begin() as conn:
#         await conn.run(Base.metadata.create_all(engine_test))
#     yield
#     async with engine_test.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all(engine_test))



