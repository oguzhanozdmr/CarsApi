from flask import Flask

app = Flask(__name__)

from cars_api import routes
from .get_json import CarFilters
