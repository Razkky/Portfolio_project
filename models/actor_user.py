#!/usr/bin/python3
"""This module define actors and user relationship"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class ActorUser(Base, BaseModel):
    """This class define actors"""

    __tablename__ = "user_actor"
    user_id = Column(Integer, ForeignKey('users.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))

