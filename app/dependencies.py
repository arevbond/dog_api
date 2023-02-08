from fastapi import Depends, HTTPException

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from database import models
from database.database import SessionLocal


def get_db():
    """Создание сессии с базой данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_image(db: Session = Depends(get_db), n: int = 1):
    """Возвращает список url'ов image объектов"""
    images = db.scalars(select(models.Image).order_by(func.random()).limit(n)).all()
    if not images:
        raise HTTPException(status_code=501, detail="Oops! Someone stole our images!")
    return [image.url for image in images]

# def get_image(db: Session = Depends(get_db)):
#     """Возвращаие url image"""
#     image = db.execute(select(models.Image).order_by(func.random())).scalar()
#     if not image:
#         raise HTTPException(status_code=501, detail="Oops! Someone stole our images!")
#     return image.image_url
