"""This module define all api for actor table"""
from api.views import app_view
from flask import jsonify, make_response, abort, request
from models.actors import Actor
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

@app_view.route('/actor/', methods=["POST"], strict_slashes=False)
def create_actor():
    """Create a new actor model"""
    #check for user input
    if not request.get_json():
        abort(404, "Not a Json")
    elif "name" not in request.get_json():
        abort(404, "No actor name")
    data = request.get_json()
    actor = Actor(**data)
    storage.new(actor)
    storage.save()
    return make_response(jsonify(actor.to_dict()), 201)

@app_view.route('/actor/<int:id>', methods=["DELETE"], strict_slashes=False)
def delete_actor(id):
    """Delete an actor from the database"""
    actor = storage.get(Actor, id)
    storage.delete(actor)
    storage.save()
    return make_response(jsonify({}), 200)