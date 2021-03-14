from os import environ

import requests
import json
from flask import render_template, request, Blueprint, jsonify
from flask_googlemaps import Map
import pickle
import numpy as np

main = Blueprint('main', __name__)


@main.route('/')
def index():
    gmap = Map(
        identifier="gmap",
        varname="gmap",
        lat=42.698334,
        lng=23.319941,
        zoom=5,
        region="BG",
        style="height:100%;width:100%;margin:0;",
    )

    return render_template('index.html', gmap=gmap)


@main.route('/info', methods=['POST'])
def get_info():
    req = request.get_json(force=True)

    latitude = req.get('latitude')
    longitude = req.get('longitude')

    weather_info = get_weather_info1(latitude, longitude)

    model_coef = pickle.load(open('../model/models/model-coef.pkl', 'rb'))

    temperature = weather_info[0]
    direction = weather_info[3]
    humidity = weather_info[2]
    oxygen = weather_info[1]
    weather_info.pop(3)
    final = [np.array(weather_info)]
    prediction = model_coef.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    
    return jsonify({'fire_coef': output, 'temp': temperature, 'humidity': humidity, 'direction': direction})


def api_call(lat, lng):
    api_key = environ.get('WEATHER_API_KEY')
    weather_api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lng}&key={api_key}'
    weather_info = requests.get(weather_api_url)
    weather_json = json.loads(weather_info.text).get('data')[0]

    return  weather_json


def get_weather_info1(lat, lng):
    weather_json = api_call(lat, lng)
    data = [weather_json.get('temp'), 41, weather_json.get('rh'), weather_json.get('wind_cdir')]

    return data


def get_weather_info2(lat, lng):
    weather_json = api_call(lat, lng)
    data = {
        'temp': weather_json.get('temp'),
        'RH': weather_json.get('rh'),
        'wind': weather_json.get('wind_spd') * 3.6,
        'rain': weather_json.get('precip'),
        'month': 'mar',
        'day': 'sun',
    }

    return data


if __name__ == '__main__':
    main.app.run()
