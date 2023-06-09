"""Define api for our genre model"""
from flask import make_response, abort, jsonify, request
from api.views import app_view
from models.genre import Genre
from models.user import User
from models import storage

@app_view.route('/genres', methods=["GET"], strict_slashes=False)
def get_genres():
    """Get all genres in database"""
    genre_list = []
    genres = storage.all(Genre)
    for genre in genres.values():
        genre_list.append(genre.to_dict())

    return make_response(jsonify(genre_list), 200)

@app_view.route('/genre/<int:id>', methods=["GET"], strict_slashes=False)
def get_genre(id):
    """Get a genre by its id"""
    genre = storage.get(Genre, id).to_dict()
    return make_response(jsonify(genre), 200)

@app_view.route('/genre/<int:user_id>', methods=["POST"], strict_slashes=False)
def create_genre(user_id):
    """Add a new genre to database"""
    #Check for user input
    if not request.get_json():
        abort(404, "Not a json")
    if 'name' not in request.get_json():
        abort(404, "No name for genre")
    data = request.get_json()
    user = storage.get_by_id(User, user_id)
    genres = storage.all(Genre)
    test = True
    if data['name']:
        for genre in genres.values():
            if genre.name == data['name']:
                print(f"checking genre name {genre.name} == {data['name']}")
                test = False
                user.genres.append(genre)
        if test:
            print('creating new genre')
            genre = Genre(**data)
            user.genres.append(genre)
            storage.new(genre)
        storage.save()
        return make_response(jsonify(genre.to_dict()), 201)
    else:
        return make_response(jsonify({}), 200)

@app_view.route('/genre/<int:id>', methods=["DELETE"], strict_slashes=False)
def delete_genre(id):
    """Delete a genre from the database"""
    genre = storage.get(Genre, id)
    user_id = request.get_json().user_id
    user = storage.get_by_id(User, user_id)
    genres = user.genres
    for genre in genres:
        if genre.id == id:
            user.genres.delete(genre)
    storage.save()
    return make_response(jsonify({}), 200)