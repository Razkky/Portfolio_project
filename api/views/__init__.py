"""Api blueprints for our application"""
from flask import Blueprint

app_view = Blueprint("app_view", __name__, url_prefix="/api")

from api.views.users import *
from api.views.actors import *
from api.views.genres import *