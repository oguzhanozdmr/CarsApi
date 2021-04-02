# -*- coding: utf-8 -*-
"""
    @author= Adem Oğuzhan Özdemir
    @email = ademoguzhanozdmr@gmail.com
    @version = 1.0
"""
from os.path import isfile
from configparser import ConfigParser
from cars_api import app, CarFilters


def create_car_filters_json():
    """
    create json for car filters
    """
    car_filters = CarFilters()
    car_filters.save_filter()


def main():
    """
    running server
    """
    if isfile('./cars_config_2.ini'):
        parser = ConfigParser()
        parser.read('./cars_config_2.ini')
        json_path = parser.get('files', 'filter_path')
        if isfile(json_path):
            app.run(debug=True)
        else:
            create_car_filters_json()
            print("json have been created. Run it again")
    else:
        print("Config.ini is missing")


if __name__ == '__main__':
    main()
