#!/usr/bin/python3
"""This module define genre and user relationship"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class GenreUser(Base):
    """This class define actors"""

    __tablename__ = "genre_actor"
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)

    user = relationship("User", backref="genre_actor", cascade="all, delete")
    genre = relationship("Genre", backref="genre_actor", cascade="all, delete")

