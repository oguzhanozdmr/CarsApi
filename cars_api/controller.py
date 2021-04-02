# -*- coding: utf-8 -*-
import json
from flask import request
from configparser import ConfigParser
from os.path import isfile
from cars_api.get_json import GetJson, create_dict

config = ConfigParser()
config.read('../CarsApi/cars_config_2.ini')


def read_filters():
    path = config['files']['filter_path']
    assert isfile(path), 'Car filters not found'

    with open(path, 'r') as file:
        filters = json.load(file)
        file.close()
    return filters


def args_to_query(args):
    config.sections()
    header = config['query_header']
    _filter = read_filters()
    query = ''
    to_query = config['header_to_cars_api']

    if header['exterior_color'] in args:
        exterior_color = args.get(header['exterior_color']).lower()
        if exterior_color in _filter['colors']:
            color_id = _filter['colors'][exterior_color]
            query += f'{to_query["exterior_color"]}={color_id}&'

    if header['brand'] in args:
        brand = args.get(header['brand']).lower()
        if brand in _filter['brands']:
            brand_id = _filter['brands'][brand]
            query += f'{to_query["brand"]}={brand_id}&'

    if header['year'] in args:
        year = args.get(header['year'])
        if year in _filter['years']:
            year_id = _filter['years'][year]
            query += f'{to_query["year"]}={year_id}&'

    if header['trans_type'] in request.args:
        trans_type = request.args.get( header['trans_type']).lower()
        if trans_type in _filter['trans']:
            trans_id = _filter['trans'][trans_type]
            query += f'{to_query["trans_type"]}={trans_id}&'

    query = f"?perPage={config['request_settings']['per_page']}&{query}"
    return query[:-1]


def car_list(args):
    query = args_to_query(args)
    get_json = GetJson(query=query)
    return create_dict(get_json.get_requests())
