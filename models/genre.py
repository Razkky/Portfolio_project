"""This module define the genre class"""

from enum import unique
from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Genre(BaseModel, Base):
    """This class defines a genre object"""

    __tablename__ = "genres"
    name = Column(String(60), nullable=True, unique=True)
    user_genre = relationship("GenreUser", backref="genres", cascade="all, delete")
