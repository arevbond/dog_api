import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_PORT, DB_NAME, DB_USER, DB_PASS, DB_HOST

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
abs_db_path = os.path.join(path, "app/sql_app.db")


# SQLALCHEMY_DATABASE_URL = f"sqlite:///{abs_db_path}"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
