# -*- coding: utf-8 -*-
# pylint: disable=C0114:
# pylint: disable=C0115:
# pylint: disable=C0116:
from typing import Any


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(x: Any):
    assert isinstance(x, list)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class CarInfo:
    def __init__(self,
                 header: str = None,
                 image_url: list = None,
                 price: int = None,
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
        self._car_header = from_str(value)

    @property
    def price(self):
        return self._car_price

    @price.setter
    def price(self, value):
        self._car_price = from_int(value)

    @property
    def brand(self):
        return self._car_brand

    @brand.setter
    def brand(self, value):
        self._car_brand = from_str(value)

    @property
    def year(self):
        return self._car_year

    @year.setter
    def year(self, value):
        self._car_year = from_int(value)

    @property
    def exterior_color(self):
        return self._car_exterior_color

    @exterior_color.setter
    def exterior_color(self, value):
        self._car_exterior_color = from_str(value)

    @property
    def trans_type(self):
        return self._car_trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._car_trans_type = from_str(value)

    @property
    def image(self):
        return self._car_image

    @image.setter
    def image(self, value):
        self._car_image = from_list(value)
