from flask import Blueprint

charity_web = Blueprint('charity-web', __name__, static_folder='static', template_folder='templates')

charity_api = Blueprint('charity-api', __name__,  static_folder='static', template_folder='templates')

from charity.views import route, api_route
