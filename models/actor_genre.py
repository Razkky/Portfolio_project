#!/usr/bin/python3
"""This module define genre and user relationship"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class GenreUser(Base, BaseModel):
    """This class define actors"""

    __tablename__ = "genre_user"
    user_id = Column(Integer, ForeignKey('users.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
