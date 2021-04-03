# -*- coding: utf-8 -*-
"""
    Cars Api unittest
"""
try:
    import requests
    import unittest
    from cars_api import app, CarInfo, controller
    from werkzeug.datastructures import MultiDict, ImmutableMultiDict
    from flask import json
except Exception as ex:
    print(f'Missing {ex}')


class FlaskTest(unittest.TestCase):
    main_path = '/cars/list'

    def test_car_list(self):
        tester = app.test_client(self)
        response = tester.get(self.main_path)
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_content(self):
        tester = app.test_client(self)
        response = tester.get(self.main_path)
        self.assertEqual(response.content_type, 'application/json')

    def test_car_list_brand(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}?brand=BMW')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_year(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}?year=2020')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_color(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}?color=black')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_trans(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}?trans=automatic')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_multi(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}?trans=automatic&brand=BMW&color=black&year=2020')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_model(self):
        car = CarInfo(header='2020  BMW 330 i xDrive',
                      brand='BMW',
                      exterior_color='Grey',
                      image_url=["https://www.cstatic-images.com/phototab/in/v1/70150921/3MW5R7J07L8B21523"
                                 "/fe8257bead7a444be4710daa1c430ea0.jpg"],
                      price=30950,
                      trans_type='Automatic',
                      year=2020)
        self.assertEqual(car.header, '2020  BMW 330 i xDrive', msg='wrong header')
        self.assertEqual(car.brand, 'BMW', msg='wrong BMW')
        self.assertEqual(car.exterior_color, 'Grey', msg='wrong color')
        self.assertEqual(car.image, ["https://www.cstatic-images.com/phototab/in/v1/70150921/3MW5R7J07L8B21523"
                                     "/fe8257bead7a444be4710daa1c430ea0.jpg"], msg='wrong photo link')
        self.assertEqual(car.price, 30950, msg='wrong price')
        self.assertEqual(car.trans_type, 'Automatic', msg='wrong Type')
        self.assertEqual(car.year, 2020, msg='wrong year')

    def test_return_count(self):
        tester = app.test_client(self)
        response = tester.get(f'{self.main_path}')
        if response.status_code == requests.codes.ok:
            data = json.loads(response.data)['cars']
            self.assertEqual(len(data), 50, msg='cars count is missing')
        self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_brand_control(self):
        brands = ['bmw', 'audi', 'ford']
        for brand in brands:
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?brand={brand}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['brand']).lower(), str(brand).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_year_control(self):
        years = ['2020', '1990', '2017']
        for year in years:
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?year={year}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['year']).lower(), str(year).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_trans_control(self):
        trans_types = ['manual', 'automatic']
        for trans in trans_types:
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?trans={trans}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['trans_type']).lower(), str(trans).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_color_control(self):
        colors = ['black', 'Black', 'white', 'RED']
        for color in colors:
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?extcolor={color}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['exterior_color']).lower(), str(color).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_two_params_control(self):
        colors = ['black', 'Black', 'white', 'RED']
        brands = ['bmw', 'audi', 'FORD']
        for color, brand in zip(colors, brands):
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?extcolor={color}&brand={brand}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['exterior_color']).lower(), str(color).lower())
                self.assertEqual(str(data['brand']).lower(), str(brand).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_three_params_control(self):
        years = ['2020', '1990']
        brands = ['bmw', 'audi']
        trans_types = ['manual', 'automatic']
        for year, trans, brand in zip(years, brands, trans_types):
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?trans={trans}&brand={brand}&year={year}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['trans_type']).lower(), str(trans).lower())
                self.assertEqual(str(data['year']).lower(), str(year).lower())
                self.assertEqual(str(data['brand']).lower(), str(brand).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')

    def test_for_params_control(self):
        years = ['2010', '2015']
        colors = ['black', 'blue']
        brands = ['bmw', 'audi']
        trans_types = ['manual', 'automatic']
        for year, trans, brand, color in zip(years, trans_types, brands, colors):
            tester = app.test_client(self)
            response = tester.get(f'{self.main_path}?brand={brand}&year={year}&trans={trans}&extcolor={color}')
            json_data = json.loads(response.data)['cars']
            self.assertTrue(json_data, msg='The list is empty')
            for data in json_data:
                self.assertEqual(str(data['trans_type']).lower(), str(trans).lower())
                self.assertEqual(str(data['year']).lower(), str(year).lower())
                self.assertEqual(str(data['brand']).lower(), str(brand).lower())
                self.assertEqual(str(data['exterior_color']).lower(), str(color).lower())
            self.assertEqual(response.status_code, requests.codes.ok, msg=f'status code {response.status_code}')





if __name__ == '__main__':
    unittest.main()
