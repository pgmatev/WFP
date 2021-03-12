from flask import Flask
from flask_googlemaps import GoogleMaps
from os import environ


google_maps = GoogleMaps()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['GOOGLEMAPS_KEY'] = environ.get('GOOGLEAPIS_KEY')

    google_maps.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
