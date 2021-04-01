from flask import Flask
from .controller import car_list

app = Flask(__name__)

from cars_api import routes
from .get_json import CarFilters


