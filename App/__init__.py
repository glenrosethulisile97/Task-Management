from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
from flask_jwt_extended import JWTManager

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    with app.app_context():
       from .routes import user_routes
       app.register_blueprint(user_routes.app)

        
    return app

