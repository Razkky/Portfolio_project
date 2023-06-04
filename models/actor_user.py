#!/usr/bin/python3
"""This module define actors and user relationship"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class ActorUser(Base):
    """This class define actors"""

    __tablename__ = "user_actor"
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    actor_id = Column(Integer, ForeignKey('actors.id'), primary_key=True)

    user = relationship("User", backref="user_actors", cascade="all, delete")

