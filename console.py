#!/usr/bin/python3
"""A console for the movie Recommendation Project"""

import cmd
from models.base import BaseModel
from models.user import User
from models.actors import Actor
from models.genre import Genre
from models import storage
import shlex  # for splitting the line along spaces except in double quotes


class MovieCommand(cmd.Cmd):
    """A Movie console to interact with our movies models and data"""

    prompt = "(Movies) "
    # Dictionary conataining the models of the application
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Actor": Actor,
               "Genre": Genre}

    def do_EOF(self, arg):
        """Exit console on EOF"""
        return True

    def do_quit(self, arg):
        """Exit console on quit command"""
        return True

    def do_create(self, arg):
        """Create a new Model
            usage1: create Model
            usage2: create Model attr1=value1 attr2=value2
        """
        # Split arguments into list
        args = shlex.split(arg)
        model = args[0]
        attributes = args[1:]
        new_dict = {}
        for attr in attributes:
            words = attr.split('=')
            key = words[0]
            value = words[1].strip("")
            new_dict[key] = value
        if len(arg) < 1:
            print("**Model name is missing**")
        elif model not in MovieCommand.classes:
            print("**Invalid model**")
        else:
            model = MovieCommand.classes[model](**new_dict)
            print(model.name)
            storage.new(model)
            storage.save()

    def do_show(self, arg):
        """Show A model base on its id
            usage: show Model id"""

        # Split arguments into list
        new_arg = shlex.split(arg)
        if len(new_arg) < 1:
            print("**Model name is missing**")
        elif new_arg[0] not in MovieCommand.classes.keys():
            print("**Invalid Model")
        elif len(new_arg) < 2:
            print("**Instance is missing**")
        else:
            instance = storage.get(MovieCommand.classes[new_arg[0]], new_arg[1])
            if instance:
                print(instance.to_dict())
            if not instance:
                print("**No instance found**")

    def do_destroy(self, arg):
        """Destroy an instance base on id
            usage: destroy Model id"""
        new_arg = shlex.split(arg)
        model = new_arg[0]
        id = new_arg[1]
        if len(new_arg) < 1:
            print("**Model name is missing**")
        elif model not in MovieCommand.classes.keys():
            print("**Invalid Model")
        elif len(new_arg) < 2:
            print("**Instance is missing**")
        else:
            model = storage.get(MovieCommand.classes[new_arg[0]], new_arg[1])
            if model:
                storage.delete(model)
                storage.save()
            else:
                print("**No instance found**")

    def do_all(self, arg):
        """Print all Models
            usage1: all (list all models)
            usage1: all Model (list all instance of this model)
        """
        # Split arguments into list
        new_arg = shlex.split(arg)
        if len(new_arg) == 0:
            all = storage.all()
            for key, value in all.items():
                print(value)
        if len(new_arg) == 1:
            model = new_arg[0]
            if model not in MovieCommand.classes.keys():
                print("**Invalid Model")
            else:
                models = storage.all()
                for key, value in models.items():
                    if key.startswith(model):
                        print(value)

    def do_update(self, arg):
        """Update an instance of a model
            usage: update model id attr1=value attr2=value
        """
        new_arg = shlex.split(arg)
        print(new_arg)
        model = new_arg[0]
        id = new_arg[1]
        attr = new_arg[2]
        value = new_arg[3]
        length = len(new_arg)
        if length < 1:
            print("**Model name is missing**")
        elif length == 1:
            print("**Missing instance id**")
        elif length == 2:
            print("**Missing instance attritube**")
        elif length == 3:
            print("**Missing attribute value**")
        elif model not in MovieCommand.classes.keys():
            print("**Invalid Model**")
        else:
            models = storage.all().values()
            model = MovieCommand.get_instance(models, id)
            if model not in ["id", "updated_at", "created_at"]:
                setattr(model, attr, value)
                storage.save()

    def get_instance(models, id):
        """Get a particular instance of a model using the id"""
        for model in models:
            if model.id == id:
                return model
        return False

    def do_count(self, arg):
        """Count the number of a particular Model
            usage: count Model
        """
        new_arg = shlex.split(arg)
        model = new_arg[0]
        count = 0
        models = storage.all()
        for key in models.keys():
            if key.startswith(model):
                count += 1
        print(count)


if __name__ == "__main__":
    MovieCommand().cmdloop()
