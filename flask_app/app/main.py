from flask import render_template, request, Blueprint, jsonify
from flask_googlemaps import Map
import requests
from os import environ


main = Blueprint('main', __name__)


@main.route('/')
def index():
    gmap = Map(
        identifier="gmap",
        varname="gmap",
        lat=42.698334,
        lng=23.319941,
        zoom=14,
        region="BG",
        style="height:100%;width:100%;margin:0;",
    )

    return render_template('index.html', gmap=gmap)


@main.route('/info', methods=['POST'])
def get_info():
    req = request.get_json(force=True)

    latitude = req.get('latitude')
    longitude = req.get('longitude')

    weather_info = get_weather_info(latitude, longitude)

    # fire_coef = algorithm(weather_info)
    fire_coef = 0.57
    fire_coef1 = 0.1

    return jsonify({'fire_coef': fire_coef, 'fire_coef1': fire_coef1})


def get_weather_info(lat, lng):
    api_key = environ.get('WEATHER_API_KEY')
    weather_api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lng}&key={api_key}'
    weather_info = requests.get(weather_api_url)

    print(weather_info.content.decode())

    return 'ok'


if __name__ == '__main__':
    main.app.run()
