from os import environ

import requests
import json
from flask import render_template, request, Blueprint, jsonify
from flask_googlemaps import Map

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

    return jsonify({'fire_coef': fire_coef})


def get_weather_info(lat, lng):
    api_key = environ.get('WEATHER_API_KEY')
    weather_api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lng}&key={api_key}'
    weather_info = requests.get(weather_api_url)
    weather_json = json.loads(weather_info.text).get('data')[0]

    data = [weather_json.get('temp'), 21, weather_json.get('rh')]
    return data


if __name__ == '__main__':
    main.app.run()
