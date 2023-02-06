import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    image: Mapped[list["Image"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    category_id = mapped_column(ForeignKey("category.id"))

    category: Mapped[Category] = relationship(back_populates="image")

    def __repr__(self):
        return f"Image(id={self.id!r}, url={self.image_url!r}, category_id={self.category_id!r})"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    create_at: Mapped[datetime.datetime]
