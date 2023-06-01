#!/usr/bin/python3
"""The module defines the user model"""
from models.base import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Define the user model"""

    __tablename__ = "users"
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    username = Column(String(60), nullable=False, unique=True)
    actors = relationship("Actor", cascade="all, delete")
    genres = relationship("Genre", cascade="all, delete")
