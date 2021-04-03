# -*- coding: utf-8 -*-
import json
from flask import request
from configparser import ConfigParser
from os.path import isfile
from cars_api.get_json import GetJson, create_dict

CONFIG = ConfigParser()
CONFIG.read('../CarsApi/cars_config.ini')
HEADER = CONFIG['query_header']


def read_filters():
    path = CONFIG['files']['filter_path']
    assert isfile(path), 'Car filters not found'

    with open(path, 'r') as file:
        filters = json.load(file)
        file.close()
    return filters


FILTER = read_filters()


def read_exterior_color_id(args):
    exterior_color = args.get(HEADER['exterior_color']).lower()
    if exterior_color in FILTER['colors']:
        color_id = FILTER['colors'][exterior_color]
        return color_id


def read_brand_id(args):
    brand = args.get(HEADER['brand']).lower()
    if brand in FILTER['brands']:
        brand_id = FILTER['brands'][brand]
        return brand_id


def read_year_id(args):
    year = args.get(HEADER['year'])
    if year in FILTER['years']:
        year_id = FILTER['years'][year]
        return year_id


def read_trans_type_id(args):
    trans_type = request.args.get(HEADER['trans_type']).lower()
    if trans_type in FILTER['trans']:
        trans_id = FILTER['trans'][trans_type]
        return trans_id


def args_to_query(args):
    query = f"?perPage={CONFIG['request_settings']['per_page']}&"
    to_query = CONFIG['header_to_cars_api']

    if HEADER['brand'] in args:
        brand_id = read_brand_id(args)
        if brand_id:
            query += f'{to_query["brand"]}={brand_id}&'
        else:
            return None

    if HEADER['trans_type'] in request.args:
        trans_type_id = read_trans_type_id(args)
        if trans_type_id:
            query += f'{to_query["trans_type"]}={trans_type_id}&'
        else:
            return None

    if HEADER['year'] in args:
        year_id = read_year_id(args)
        if year_id:
            query += f'{to_query["year"]}={year_id}&'
        else:
            return None

    if HEADER['exterior_color'] in args:
        color_id = read_exterior_color_id(args)
        if color_id:
            query += f'{to_query["exterior_color"]}={color_id}&'
        else:
            return None

    return query[:-1]


def car_list(args):
    query = args_to_query(args)
    if query:
        get_json = GetJson(query=query)
        return create_dict(get_json.get_requests())
    return {'cars': []}
