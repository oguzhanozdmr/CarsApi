# -*- coding: utf-8 -*-
import json
from flask import request
from configparser import ConfigParser
from os.path import isfile
from cars_api.get_json import GetJson
from .model import CarInfo
from .html_scraping import Scraping


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


def create_dict(json_data) -> dict:
    """
    creating new dict
    """
    car_detail_dict = {'cars': []}
    html_scraping = Scraping(json_data['html']['listings'])
    car_json_detail = json_data['dtm']['vehicle']
    for car_detail in car_json_detail:
        car = CarInfo()
        car.header = f"{car_detail['year']} {car_detail['make']} {car_detail['model']} {car_detail['trim']}"
        car.image, car.exterior_color, car.trans_type = html_scraping.get_data(car_detail['listingId'])
        car.price = car_detail['price']
        car.brand = f"{car_detail['make']}"
        car.year = car_detail['year']
        car_detail_dict['cars'].append(car.to_dict())
    return car_detail_dict


def car_list(args):
    query = args_to_query(args)
    if query:
        get_json = GetJson(query=query)
        return create_dict(get_json.get_requests())
    return {'cars': []}
