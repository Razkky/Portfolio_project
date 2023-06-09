#!/usr/bin/python3
"""Contains the base model for the movie project"""
import sys
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DATETIME, Integer
from sqlalchemy.ext.declarative import declarative_base
sys.path.append("..")

Base = declarative_base()


class BaseModel():
    """A base model for other models"""
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Initialize base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the model"""
        new_dict = {}
        new_dict.update(self.__dict__)
        del new_dict['_sa_instance_state']
        return f"[{self.__class__.__name__}] [{self.id}] {new_dict}"

    def save(self):
        from models import storage
        """Save model"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dictionary representation of model"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        new_dict["__class__"] = self.__class__.__name__
        del new_dict["_sa_instance_state"]
        return new_dict
