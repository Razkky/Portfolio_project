"""This module define the genre class"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Genre(BaseModel, Base):
    """This class defines a genre object"""

    __tablename__ = "genres"
    name = Column(String(60), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
