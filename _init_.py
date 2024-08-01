# from flask import Flask
# from flaskpymongo import PyMongo
# from config import Config

# Initialize the Flask app
#  def createapp():
#     app = Flask(__name)
#     app.config.from_object(Config)

# Initialize extensions
#     mongo = PyMongo()
#     mongo.init_app(app)

#     # Register blueprints
#     from .routes import auth_bp
#     app.register_blueprint(auth_bp, url_prefix='/auth')

#     return app