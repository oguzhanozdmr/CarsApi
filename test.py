# -*- coding: utf-8 -*-
"""
    Cars Api unittest
"""
try:
    import requests
    import unittest
    from cars_api import app, CarInfo, controller
    from werkzeug.datastructures import MultiDict, ImmutableMultiDict

except Exception as ex:
    print(f'Missing {ex}')


class FlaskTest(unittest.TestCase):
    def test_car_list(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_content(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list')
        self.assertEqual(response.content_type, 'application/json')

    def test_car_list_brand(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list?brand=BMW')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_year(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list?year=2020')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_color(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list?color=black')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_trans(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list?trans=automatic')
        self.assertEqual(response.status_code, requests.codes.ok)

    def test_car_list_multi(self):
        tester = app.test_client(self)
        response = tester.get('/cars/list?trans=automatic&brand=BMW&color=black&year=2020')
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
        self.assertEqual(car.header, '2020  BMW 330 i xDrive')
        self.assertEqual(car.brand, 'BMW')
        self.assertEqual(car.exterior_color, 'Grey')
        self.assertEqual(car.image, ["https://www.cstatic-images.com/phototab/in/v1/70150921/3MW5R7J07L8B21523"
                                     "/fe8257bead7a444be4710daa1c430ea0.jpg"])
        self.assertEqual(car.price, 30950)
        self.assertEqual(car.trans_type, 'Automatic')
        self.assertEqual(car.year, 2020)


if __name__ == '__main__':
    unittest.main()
