from flask import Flask, render_template, request, redirect, url_for, Blueprint
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


if __name__ == '__main__':
    main.app.run()
