#!/usr/bin/python3
"""This module define actors"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Actor(BaseModel, Base):
    """This class define actors"""

    __tablename__ = "actors"
    name = Column(String(60), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
