from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Register Blueprints
    app.register_blueprint(main)

    return app
