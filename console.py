#!/usr/bin/python3
"""A console for the movie Recommendation Project"""

import cmd
from werkzeug.security import generate_password_hash
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
            if model in ["Actor", "Genre"]:
                user = storage.get_by_id(User, new_dict['user_id'])
                items = storage.all(MovieCommand.classes[model])
                test = True
                for item in items.values():
                    if item.name == new_dict['name']:
                        model = storage.get_by_id(MovieCommand.classes[model], item.id)
                        print(model)
                        if type(model) == MovieCommand.classes['Actor']:
                            user.actors.append(model)
                            test = False
                        else:
                            print("creating gnere")
                            user.genres.append(model)
                            test = False

                if test:
                    del new_dict['user_id']
                    new_dict['user_id'] = user.id
                    model = MovieCommand.classes[model](**new_dict)
                    if type(model) == MovieCommand.classes['Actor']:
                        user.actors.append(model)
                    else:
                        user.genres.append(model)
            else:
                model = MovieCommand.classes[model](**new_dict)
                model.password = generate_password_hash(model.password)
                print(model.password)
            print(model.name)
            storage.new(model)
            storage.save()

    def do_show(self, arg):
        """Show A model base on its id
            usage: show Model id"""

        # Split arguments into list
        new_arg = shlex.split(arg)
        model = new_arg[0]
        if len(new_arg) < 1:
            print("**Model name is missing**")
        elif new_arg[0] not in MovieCommand.classes.keys():
            print("**Invalid Model")
        elif len(new_arg) < 2:
            print("**Instance is missing**")
        else:
            new_dict ={}
            for attr in new_arg[1:]:
                words = attr.split('=')
                key = words[0]
                value = words[1].strip("")
                new_dict[key] = value
            instance = storage.get_by_id(MovieCommand.classes[model], new_dict['id'])
            if instance:
                print(instance.to_dict())
            if not instance:
                print("**No instance found**")

    def do_destroy(self, arg):
        """Destroy an instance base on id
            usage: destroy Model id"""
        new_arg = shlex.split(arg)
        model = new_arg[0]
        attrs = new_arg[1:]
        new_dict = {}
        for attr in attrs:
            words = attr.split('=')
            key = words[0]
            value = words[1].strip("")
            new_dict[key] = value
        id = new_arg[1]
        if len(new_arg) < 1:
            print("**Model name is missing**")
        elif model not in MovieCommand.classes.keys():
            print("**Invalid Model")
        elif len(new_arg) < 2:
            print("**Instance is missing**")
        else:
            if model == "Actor":
                user = storage.get_by_id(User, new_dict['user_id'])
                actors = user.actors
                for actor in actors:
                    if actor.id == int(new_dict['id']):
                        print("removing actor")
                        user.actors.remove(actor)
                        storage.save()
            if model == "Genre":
                user = storage.get_by_id(User, new_dict['user_id'])
                genres = user.genres
                for genre in genres:
                    if actor.id == int(new_dict['id']):
                        print("removing genre")
                        user.actors.remove(genre)
                        storage.save()

            else:
                model = storage.get_by_id(MovieCommand.classes[model], new_dict['id'])
                for actor in model.actors:
                    model.actors.remove(actor)
                for genre in model.genres:
                    model.genres.remove(genre)
                print(model)
                storage.delete(model)
                storage.save()

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
