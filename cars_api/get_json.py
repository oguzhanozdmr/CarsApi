# -*- coding: utf-8 -*-
# pylint: disable=C0114:
# pylint: disable=C0115:
# pylint: disable=C0116:
import requests
import json
from configparser import ConfigParser


class GetJson:
    def __init__(self,
                 protocol: str = 'https://',
                 domain_name: str = 'www.cars.com',
                 path: str = '/for-sale/listings/',
                 query: str = ""):
        if protocol and domain_name and path:
            self._domain_url = protocol + domain_name + path + query
        config = ConfigParser()
        config.read('../CarsApi/cars_config_2.ini')
        self._headers = config['request_header']

    def get_requests(self):
        if self._domain_url:
            json_request = requests.get(self._domain_url, headers=self._headers)
            if json_request.status_code == requests.codes.ok:
                return json_request.json()
        return None


class CarFilters(GetJson):
    _class_filters = {'brand': 3, 'year': 2, 'color': 6, 'trans': 10}

    def __init__(self):
        super().__init__()
        self._car_json_data = super().get_requests()['json']['filters']['allFilters']

    def get_brand_id(self):
        brands_dic = {}
        if self._car_json_data:
            brands = self._car_json_data[self._class_filters['brand']]['values']
            for brand in brands:
                brands_dic[brand['name']] = brand['id']
        return brands_dic

    def get_year_id(self):
        years_dic = {}
        if self._car_json_data:
            years = self._car_json_data[self._class_filters['year']]["values"]
            for year in years:
                years_dic[year['name']] = year['id']
        return years_dic

    def get_color_id(self):
        colors_dic = {}
        if self._car_json_data:
            colors = self._car_json_data[self._class_filters['color']]["values"]
            for color in colors:
                colors_dic[color['name']] = color['id']
        return colors_dic

    def get_trans_type_id(self):
        trans_types_dic = {}
        if self._car_json_data:
            types = self._car_json_data[self._class_filters['trans']]["values"]
            for _type in types:
                trans_types_dic[_type['name']] = _type['id']
        return trans_types_dic

    def save_filter(self):
        brands = self.get_brand_id()
        colors = self.get_color_id()
        years = self.get_year_id()
        trans = self.get_trans_type_id()
        filters = {'brands': brands, 'colors': colors, 'years': years, 'trans': trans}
        with open("../data/car_filters.json", "w+") as file:
            json.dump(filters, file, indent=4, sort_keys=True)
            file.close()

if __name__ == '__main__':
    cc = CarFilters()
    print(cc.get_brand_id())
    cc.save_filter()
    #print(cc.get_trans_type_id())
    #print(cc.get_color_id())
    #print(cc.get_year_id())



















"""
# -*- coding: utf-8 -*-


https://stackoverflow.com/questions/50918276/deploying-flask-app-on-cherrypy-server/50949979

install cherrypy:
    conda install -c anaconda cherrypy


try:
    from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer, WSGIPathInfoDispatcher as PathInfoDispatcher

import time
from flask import Flask
app1 = Flask(__name__)

app1.secret_key = 'abcdef'

@app1.route('/u1')
def hello():
    print("başladı")
    time.sleep(6)
    print("bitti1")


if __name__ == '__main__':
   # app1.run()
    dispatcher = PathInfoDispatcher({'/': app1})
    server = WSGIServer(("127.0.0.1", 8091), dispatcher)
    server.start()
"""
