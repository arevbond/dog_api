from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from ..dependencies import get_image

router = APIRouter(
    prefix="/home",
    tags=["home"]
)

templates = Jinja2Templates(directory="templates")

"""Рабочий код, но он не использует Depends(исправил кодом ниже!)"""


# @router.get("/", response_class=HTMLResponse)
# async def home(request: Request, db: Session = Depends(get_db)):
#     """Функция работает, но хочется совместить с кодом из image.get_dog_image"""
#
#     image = db.execute(select(models.Image).order_by(func.random())).scalar()
#     img_url = "/images/" + '/'.join(image.image_url.split('/')[-2:])
#
#     return templates.TemplateResponse("index.html", {"request": request, "img_url": img_url})


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, images: str = Depends(get_image)):
    """Функция получает список url'ов Image объектов, преобразовывает их в список абсолютных url'ов"""
    imgs_url = []
    for img in images:
        url = "/images/" + '/'.join(img.split('/')[-2:])
        imgs_url.append(url)
    return templates.TemplateResponse("index.html", {"request": request, "imgs_url": imgs_url})
