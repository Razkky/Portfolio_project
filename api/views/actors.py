"""This module define all api for actor table"""
from api.views import app_view
from flask import jsonify, make_response, abort, request
from models.actors import Actor
from models.user import User
from models import storage

@app_view.route('/actors', methods=["GET"], strict_slashes=False)
def get_actors():
    """Get all actors from database"""
    actors_list = []
    actors = storage.all(Actor)
    for actor in actors.values():
        actors_list.append(actor.to_dict())
    return make_response(jsonify(actors_list), 200)

@app_view.route('/actor/<int:id>', methods=["GET"], strict_slashes=False)
def get_actor(id):
    """Retrieve a particular actor with id"""
    actor = storage.get(Actor, id).to_dict()
    return make_response(jsonify(actor), 200)

@app_view.route('/actor/<int:user_id>', methods=["POST"], strict_slashes=False)
def create_actor(user_id):
    """Create a new actor model"""
    #check for user input
    if not request.get_json():
        abort(404, "Not a Json")
    elif "name" not in request.get_json():
        abort(404, "No actor name")
    elif "user_id" not in request.get_json():
        abort(404, "Invalid User")
    data = request.get_json()
    print(f"printing json data {data}")
    user = storage.get_by_id(User, user_id)
    actors = storage.all(Actor)
    test = True
    print("creating actor")
    if data['name']:
        for actor in actors.values():
            if actor.name == data['name']:
                print(f"checking actors name {actor.name} == {data['name']}")
                test = False
                user.actors.append(actor)
        if test:
            print("creating new actor")
            actor = Actor(**data)
            user.actors.append(actor)
            storage.new(actor)
        storage.save()
        print("saved")
        return make_response(jsonify(actor.to_dict()), 201)
    else:
        return make_response(jsonify({}), 200)


@app_view.route('/actor/<int:id>', methods=["DELETE"], strict_slashes=False)
def delete_actor(id):
    """Delete an actor from the database"""
    if not request.get_json():
        abort(404, "Not a JSon")
    user_id = request.get_json().user_id
    user = storage.get_by_id(User, user_id)
    actors = user.actors
    for actor in actors:
        if actor.id == id:
            user.actors.delete(actor)
    storage.save()
    return make_response(jsonify({}), 200)