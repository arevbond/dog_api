import os
from database import models
from database.database import SessionLocal

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
images_path = os.path.join(path, "Images")
#
# test_cat = models.Category(id=1, name="test_category_1")
# session = SessionLocal()
# session.add(test_cat)
# session.commit()


def get_images(abs_path: str):
    for current_dir, dirs, files in os.walk(abs_path):
        if not dirs:
            category_name = current_dir.split("-")[-1].capitalize()
            """В этом месте дописать создание категории в бд, если она не созданаа"""

            # print(category_name)

            # print(category_name)
            for file in files[:5]:
                """В этом месте дописать внесение файла в таблицу Image"""
                file_url = os.path.join(current_dir, file)
                print(file_url)
            print("*" * 10)


# get_images(images_path)
