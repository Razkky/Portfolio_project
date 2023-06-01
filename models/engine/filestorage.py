#!/usr/bin/python3
import sys
import json
import os


class FileStorage:
    """Save instance to a json file"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return all contents of filestorage"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Create new instance model"""
        if obj:
            key = obj.__class__.__name__ +"." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Save instance model"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(new_dict, fd)

    def reload(self):
        """Reload models from json file"""
        from models.base import BaseModel
        from models.user import User
        from models.actors import Actor
        from models.genre import Genre

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Actor": Actor,
                   "Genre": Genre}
        new_dict = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fd:
                new_dict = json.load(fd)
        for key, value in new_dict.items():
            FileStorage.__objects[key] = classes[value["__class__"]](**value)

    def delete(self, obj=None):
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            del FileStorage.__objects[key]
        
    