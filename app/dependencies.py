from database.database import SessionLocal


def get_db():
    """Создание сессии с базой данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
