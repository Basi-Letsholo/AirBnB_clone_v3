#!/usr/bin/python3
""" Api module vies init"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from api.v1.views.index import *
