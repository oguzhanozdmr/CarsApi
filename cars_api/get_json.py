# -*- coding: utf-8 -*-
import requests
import json
from configparser import ConfigParser


class GetJson:
    """
    getting Json from cars.com
    """
    def __init__(self, query: str = ""):
        config = ConfigParser()
        config.read('../CarsApi/cars_config.ini')
        self._domain_url = config['request_settings']['url'] + query
        self._headers = config['request_header']

    def get_requests(self):
        """
        getting json from cars.com
        return
        request_json
        """
        if self._domain_url:
            json_request = requests.get(self._domain_url, headers=self._headers)
            if json_request.status_code == requests.codes.ok:
                return json_request.json()
        return None


class CarFilters(GetJson):
    """
     getting car filters from cars.com
    """
    _class_filters = {'brand': 3, 'year': 2, 'color': 6, 'trans': 10}

    def __init__(self):
        super().__init__()
        self._car_json_data = super().get_requests()['json']['filters']['allFilters']

    def get_brand_id(self) -> dict:
        """
        getting make for cars.com
        return
        brand_dict: dict = brand dict value
        """
        brand_dict = {}
        if self._car_json_data:
            brands = self._car_json_data[self._class_filters['brand']]['values']
            for brand in brands:
                brand_dict[brand['name'].lower()] = brand['id']
        return brand_dict

    def get_year_id(self) -> dict:
        """
        getting year for cars.com
        return
        years_dict: dict = year dict value
        """
        years_dic = {}
        if self._car_json_data:
            years = self._car_json_data[self._class_filters['year']]["values"]
            for year in years:
                years_dic[year['name']] = year['id']
        return years_dic

    def get_color_id(self) -> dict:
        """
        getting color for cars.com
        return
        colors_dic: dict = color dict value
        """
        colors_dic = {}
        if self._car_json_data:
            colors = self._car_json_data[self._class_filters['color']]["values"]
            for color in colors:
                colors_dic[color['name'].lower()] = color['id']
        return colors_dic

    def get_trans_type_id(self) -> dict:
        """
        getting trans_type for cars.com
        return
        trans_types_dic: dict = trans_type_dic dict value
        """
        trans_types_dic = {}
        if self._car_json_data:
            types = self._car_json_data[self._class_filters['trans']]["values"]
            for _type in types:
                trans_types_dic[_type['name'].lower()] = _type['id']
        return trans_types_dic

    def save_filter(self):
        """
        saving car filters
        """
        brands = self.get_brand_id()
        colors = self.get_color_id()
        years = self.get_year_id()
        trans = self.get_trans_type_id()
        filters = {'brands': brands, 'colors': colors, 'years': years, 'trans': trans}
        with open("../CarsApi/data/car_filters.json", "w+") as file:
            json.dump(filters, file, indent=4, sort_keys=True)
            file.close()
