#!/usr/bin/python3
""" Api Status Module """

import os
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(error):
    return {
            "error": "Not found"
            }, 404


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
