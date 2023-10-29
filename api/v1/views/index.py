#!/usr/bin/python3
""" Api route module """

from api.v1.views import app_views
#from flask import Flask
#from flask import jsonify

#app = Flask(__name__)


@app_views.route('/status', strict_slashes=False, methods=["GET"])
def status():
    """Returns status"""
    status_json = {
            "status": "OK"
            }
    return (status_json)
