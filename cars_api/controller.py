from flask import jsonify, request
from configparser import ConfigParser
from os.path import isfile
import json

config = ConfigParser()
config.read('../CarsApi/cars_config_2.ini')


def read_query_header():
    config.sections()
    header = config['query_header']
    color_query = header['exterior_color']
    brand_query = header['brand']
    year_query = header['year']
    request_query = header['trans_type']
    return color_query, brand_query, year_query, request_query


def read_filters():
    path = config['files']['filter_path']
    assert isfile(path), 'Car filters not found'
    with open(path, 'r') as file:
        filters = json.load(file)
        file.close()
    return filters


def args_to_query(args):
    color_query, brand_query, year_query, request_query = read_query_header()
    _filter = read_filters()

    query = ""
    if color_query in args:
        exterior_color = args.get(color_query)
        if exterior_color in _filter["colors"]:
            color_id = _filter["colors"][exterior_color]
            query += ""

    if brand_query in args:
        brand = args.get(brand_query)
    if year_query in args:
        year = args.get(year_query)
    if request_query in request.args:
        trans_type = request.args.get(request_query)


def car_list(args):
    if args:
        query = args_to_query(args)
    read_filters()


