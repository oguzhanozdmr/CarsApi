# -*- coding: utf-8 -*-
from flask import Flask
from .controller import car_list
from .get_json import CarFilters

__version__ = '0.1.0'
__author__ = 'Adem Oguzhan OZDEMIR'
__email__ = 'ademoguzhanozdmr@gmail.com'

app = Flask(__name__)

from cars_api import routes
from cars_api.model import CarInfo
from cars_api.controller import args_to_query