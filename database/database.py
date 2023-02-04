import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
abs_db_path = os.path.join(path, "app/sql_app.db")


SQLALCHEMY_DATABASE_URL = f"sqlite:///{abs_db_path}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
