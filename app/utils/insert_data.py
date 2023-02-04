"""
Скрипт, который заливает данные в две таблицы в бд.
Обязательное расположение скрипта относительно фотографий на диске:

  Images
  app
   utils
    |--insert_data.py
"""
from database import models
from database.database import SessionLocal

import os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

images_path = os.path.join(path, "Images")  # абсолютный путь до директории Images


def insert_images_and_category_data(abs_path: str):
    """
    Функция вносит данные в табл. Category и Image беря данные из папки Images
    :param abs_path:
    :return:
    """
    session = SessionLocal()
    n = 1
    for current_dir, dirs, files in os.walk(abs_path):
        if not dirs:
            category_name = current_dir.split("-")[-1].capitalize()
            category = models.Category(name=category_name)
            session.add(category)
            for file in files:
                file_url = os.path.join(current_dir, file)
                image = models.Image(image_url=file_url, category_id=n)
                session.add(image)
            n += 1
    session.commit()


insert_images_and_category_data(images_path)
