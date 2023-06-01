
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload
from models.base import Base, BaseModel
from models.user import User
from models.actors import Actor
from models.genre import Genre


class DBStorage:
    """A class that defines the db storage engine for our application"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize database engine"""
        DB_USERNAME = 'abdul'
        DB_PASSWORD = 'aminah.aliyah'
        DB_HOST = 'localhost'
        DB_NAME = 'movie_db'
        db_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

        DBStorage.__engine = create_engine(db_url, pool_pre_ping=True)

    def all(self, cls=None):
        """Retrive all model or a particular model"""
        new_obj = {}
        all_models = {
            "User": User,
            "Actor": Actor,
            "Genre": Genre
        }

        if cls:
            models = DBStorage.__session.query(cls).all()
            for model in models:
                key = f"{model.__class__.__name__}.{model.id}"
                new_obj[key] = model
            return new_obj
        else:
            for item in all_models.values():
                models = DBStorage.__session.query(item).all()
                for model in models:
                    key = f"{model.__class__.__name__}.{model.id}"
                    new_obj[key] = model
            return new_obj

    def new(self, obj=None):
        """Add new data to database"""
        if obj:
            DBStorage.__session.add(obj)

    def save(self):
        """Save data to database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Delete data from database"""
        if obj:
            print("deleting")
            DBStorage.__session.delete(obj)
            print("about to")
            DBStorage.__session.commit()
            print("deleted")

    def reload(self):
        Base.metadata.create_all(DBStorage.__engine)
        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = scoped_session(Session)()

    def get(self, model, email):
        """Get a model with a particular id"""
        if model == User:
            model = DBStorage.__session.query(model).options(
                    joinedload(User.actors)).options(
                    joinedload(User.genres)).filter(model.email == email).one()
        else:
            model = DBStorage.__session.query(model).filter(
                    model.email == email).one()
        if not model:
            return None
        return model

    def close(self):
        """Close current sesssion to database"""
        DBStorage.__session.close()
