# Portfolio Porject
## Title: Movie Recommendation App
The Movie Recommendation System is a web application designed to address the overwhelming challenge of choosing a movie to watch from the vast selection available. This innovative solution provides users with personalized movie recommendations based on their individual preferences.

## The Console
The console is the first segment of the movie recommendation project. It is a command interpreter integrated into the app to manage object and interact with the application's backend from the command line
### Functionalities of this console:
- Create a new object to database(ex: A new user)
- Retrieve all object from database
- Update an object using the object id
- Destroy and object using the object id

## Table of Content
- **[Environment](#environment)**
- **[The console](#the-console-1)**
    - **[Installation](#installation-of-console)**
    - **[Usage](#usage)**
- **[File Descriptions](#file-description)**

## Environment
This project is interpreted/tested/installed on Ubuntu 22.04 using python3(Version 3.10)

## The console
- ## Console installation
    - Clone this repo: `git clone https://github.com/Razkky/Portfolio_project.git`
    - Navigate to the directory `cd movie_project`
    - Run the console interpreter `./console.py` and enter command
- ## Usage
    ```
    (Movies) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (Movies) count User
    2
    (Movies) create User name=Farouk email=faroukabu@gmail.com username=farouk password=rouky
    Farouk
    (Movies) count User
    3
    (Movies) all User
    [User] [4] {'password': 'kkk', 'username': 'mrcapble', 'created_at': datetime.datetime(2023, 5, 21, 14, 41, 14), 'name': 'waliy', 'email': 'waliyu.com', 'id': 4, 'updated_at': datetime.datetime(2023, 5, 21, 14, 41, 32)}
    [User] [5] {'password': 'kkkkk', 'username': 'rouky', 'created_at': datetime.datetime(2023, 5, 21, 15, 29, 54), 'name': 'farouk', 'email': 'farouk@gmail.com', 'id': 5, 'updated_at': datetime.datetime(2023, 5, 21, 15, 29, 54)}
    [User] [7] {'password': 'rouky', 'username': 'farouk', 'created_at': datetime.datetime(2023, 5, 22, 10, 9, 19), 'name': 'Farouk', 'email': 'faroukabu@gmail.com', 'id': 7, 'updated_at': datetime.datetime(2023, 5, 22, 10, 9, 19)}
    (Movies) show User 7
    {'password': 'rouky', 'username': 'farouk', 'created_at': '2023-05-22T10:09:19', 'name': 'Farouk', 'email': 'faroukabu@gmail.com', 'id': 7, 'updated_at': '2023-05-22T10:09:19', 'genres': [], 'actors': [], '__class__': 'User'}
    (Movies) destroy User 7
    (Movies) all User
    [User] [4] {'password': 'kkk', 'username': 'mrcapble', 'created_at': datetime.datetime(2023, 5, 21, 14, 41, 14), 'name': 'waliy', 'email': 'waliyu.com', 'id': 4, 'updated_at': datetime.datetime(2023, 5, 21, 14, 41, 32)}
    [User] [5] {'password': 'kkkkk', 'username': 'rouky', 'created_at': datetime.datetime(2023, 5, 21, 15, 29, 54), 'name': 'farouk', 'email': 'farouk@gmail.com', 'id': 5, 'updated_at': datetime.datetime(2023, 5, 21, 15, 29, 54)}
    (Movies)
    ```
## File Description
[console.py](console.py): The entry point of the command interpreter. This commands supported by this console includes
- `EOF` - exit the console.
- `do_quit(self, arg)` - exit the console.
- `do_create(self, arg)` - create new instance of a model.
- `do_update(self, arg)` - update any instance of a model base on its id.
- `do_destroy(self, arg)` - destroy any instance of a model base on its id.
- `do_all(self, arg)` - print all models.
- `do_count(self, arg)` - Count all object of a particular model  

**models/** directory containing all the models for the project:  
[base.py](models/base.py): The BaseModel which contains the feature that all other classes inherit. 
- `def __init__(self, *args, **kwargs)` - Initialize the model
- `def __str__(self)` - String representation of the model
- `def save(self)` - update the attribute updated_at which tells the last time the model was updated
- `def to_dict(self)` - Convert the model into dictionary object  

[user.py](models/user.py) - Defines the user table  
[actors.py](models/actor.py) - Defines the actor table  
[genres.py](modeles/genre.py) - Defines the genre table  

**models/engine** directory conataining the storage engine for the project  
[dbstorage.py](models/engine/dbstorage.py): Connnects to the database and contain all features needed to access the database
- `def __init__(self)` - Initialize the database
- `def all(self, cls=None)` - Returns all models or a particular model if cls is not None
- `def new(self, obj)` - Add new object to the database
- `def save(self)` - commits object to the database
- `def delete(self, obj=None)` - Delete an object from the database
- `def reload(self)`- Reload contents of the database
- `def get(seld, model id)` Get an object from the database using its id
- `def close(self)` - Close the database after every request


