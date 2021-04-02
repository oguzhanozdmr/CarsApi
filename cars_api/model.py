# -*- coding: utf-8 -*-
# pylint: disable=C0114:
# pylint: disable=C0115:
# pylint: disable=C0116:

class CarInfo:
    def __init__(self,
                 header: str = None,
                 image_url: list = None,
                 price: str = None,
                 brand: str = None,
                 year: int = None,
                 exterior_color: str = None,
                 trans_type: str = None):
        if image_url is None:
            # list is mutable
            image_url = []
        self._car_header = header
        self._car_image = image_url
        self._car_price = price
        self._car_brand = brand
        self._car_year = year
        self._car_exterior_color = exterior_color
        self._car_trans_type = trans_type

    def to_dict(self) -> dict:
        results = {"header": self._car_header, "image_url": self._car_image, "price": self._car_price,
                   "brand": self._car_brand, "year": self._car_year, "exterior_color": self._car_exterior_color,
                   "trans_type": self._car_trans_type}
        return results

    @property
    def header(self):
        return self._car_header

    @header.setter
    def header(self, value):
        self._car_header = value

    @property
    def price(self):
        return self._car_price

    @price.setter
    def price(self, value):
        self._car_price = value

    @property
    def brand(self):
        return self._car_brand

    @brand.setter
    def brand(self, value):
        self._car_brand = value

    @property
    def year(self):
        return self._car_year

    @year.setter
    def year(self, value):
        self._car_year = value

    @property
    def exterior_color(self):
        return self._car_exterior_color

    @exterior_color.setter
    def exterior_color(self, value):
        self._car_exterior_color = value

    @property
    def trans_type(self):
        return self._car_trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._car_trans_type = value

    @property
    def image(self):
        return self._car_image

    @image.setter
    def image(self, value):
        self._car_image = value
