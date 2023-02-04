from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from ..dependencies import get_db
from database import models

router = APIRouter(
    prefix="/api/breeds/image/random",
    tags=["dog-image"],
)


@router.get("/")
def get_dog_image(db: Session = Depends(get_db), category: str | None = None):
    """"""
    if not category:
        image = db.execute(select(models.Image).order_by(func.random())).scalar()

        if not image:
            raise HTTPException(status_code=501, detail="Oops! Someone stole our images!")

    return {"status": "success", "image": image.image_url}
