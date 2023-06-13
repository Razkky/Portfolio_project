"""Return a json object of users"""
from flask import jsonify, make_response, abort, request
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from functools import wraps
from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload
from uuid import uuid4
import os
from dotenv import load_dotenv
import jwt
from api.views import app_view
from models import storage
from models.user import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'] 
        if not token:
            return make_response(jsonify("error", "Token is missing"))

        try:
            data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
            email = data.get('email')
            user = storage.get(User, email)
        except jwt.exceptions.DecodeError:
            return make_response(jsonify({"error": "Invalid token"}), 401)
        return f(user.email)
    print(decorated)
    return decorated

@app_view.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    print("getting all users")
    """Return list of all users"""
    users_list = []
    all_users = storage.all(User)
    for user in all_users.values():
        user_dict = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "actors": [],
            "genres": []
        }
        actors = user.actors
        print("PRinting Actors")
        print(actors)
        genres = user.genres
        for actor in actors:
            #Create a dictionary with actor details
            print(actor)
            actor_dict = {
                "id": actor.id,
                "name": actor.name,
            }
            user_dict['actors'].append(actor_dict)
        for genre in genres:
            #Create a dictionary with genre details
            genre_dict = {
                "id": genre.id,
                "name": genre.name,
            }
            user_dict['genres'].append(genre_dict)
        users_list.append(user_dict)
        print(users_list)
    return jsonify(users_list)

@app_view.route('/login', methods=["POST"], strict_slashes=False)
def login():
    """Log a user in"""
    email = request.json.get('email')
    password = request.json.get('password')
    user = storage.get(User, email)
    print(user)
    if not user:
        print("no user")
        return make_response(jsonify({"error": "Invalid email or password"}))
    if check_password_hash(user.password, password):
        token = get_token(user)
        print(token)
        return make_response(jsonify({'token': token}), 200)

    return make_response(jsonify({"error": "Invalid username or Password"}), 401)

@app_view.route('/user/<email>', methods=["GET"], strict_slashes=False)
@token_required
def get_user(email):
    print('getting user')
    """Get a user with a particular id"""
    if email:
        print(email)
        user = storage.get(User, email)
        if not user:
            abort(404)
        #Dictionary that holds user details
        user_dict = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "actors": [],
            "genres": []
        }
        actors = user.actors
        genres = user.genres
        for actor in actors:
            #Create a dictionary with actor details
            actor_dict = {
                "id": actor.id,
                "name": actor.name,
            }
            user_dict['actors'].append(actor_dict)
        for genre in genres:
            #Create a dictionary with genre details
            genre_dict = {
                "id": genre.id,
                "name": genre.name,
            }
            user_dict['genres'].append(genre_dict)
        print("returning")
        return make_response(jsonify(user_dict), 200)
    return make_response(jsonify({"error": "Unauthorized access"}))


@app_view.route('/users', methods=["POST"], strict_slashes=False)
def create_user():
    print("creating")
    """Create new user to database"""
    #Check if user input is a json object and all attributes needed
    if not request.get_json():
        abort(404)
    if 'name' not in request.get_json():
        abort(404, "input name")
    if 'username' not in request.get_json():
        abort(404, "input username")
    if 'password' not in request.get_json():
        abort(404, "input password")
    if 'email' not in request.get_json():
        abort(404, "input email")
    # Get json data from user
    data = request.get_json()
    print(data)
    password = data['password']
    hashed_password = generate_password_hash(password)
    data['password'] = hashed_password
    print("printing data")
    print(data)
    user = User(**data)
    print("save user")
    storage.new(user)
    storage.save()
    print("saved user")
    user_dict = {
        "name": user.name,
        "id": user.id
    }
    return make_response(jsonify(user_dict), 200)

@app_view.route('/user/<email>', methods=["PUT"], strict_slashes=False)
@token_required
def udpate_user(email):
    """Update a particular user profile"""
    # Check for user input
    if not request.get_json():
        abort(404, "Not a Json")
    if 'id' in request.get_json():
        abort(404, "Can't change id")
    data = request.get_json()
    user = storage.get(User, email)
    ignore = ['id', 'updated_at', 'created_at']
    for key, value in data.items():
        if key == 'password':
            value = generate_password_hash(value)
        setattr(user, key, value)
    user.save()
    storage.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_view.route('/user/<email>', methods=["DELETE"], strict_slashes=False)
@token_required
def delete_user(email):
    """Delete a user from database"""
    print(id)
    user = storage.get(User, email)
    for actor in user.actors:
        user.actors.remove(actor)
    for genre in user.genres:
        user.genres.remove(genre)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)

@app_view.route('/user/reset_password', methods=['GET'], strict_slashes=False)
def reset_request():
    """Send mail to user to reset password"""
    email = request.json.get('email')
    user = storage.get(User, email)
    if user:
        token = get_token(user)

@app_view.route('/user/reset_password/<token>', methods=["GET"], strict_slashes=False)
def reset_password(token):
    """Reset Password"""
    data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    if data:
        email = data.get('email')
        user = storage.get(User, email)
    
    
def get_token(user):
    """Generate token"""
    data = {
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(data, os.environ.get('SECRET_KEY'))
    return token