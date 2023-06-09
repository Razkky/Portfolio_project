#!/usr/bin/python3
"""This module define actors"""

from enum import unique
from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Actor(BaseModel, Base):
    """This class define actors"""

    __tablename__ = "actors"
    name = Column(String(60), nullable=True, unique=True)
