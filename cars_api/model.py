# -*- coding: utf-8 -*-
from typing import Any


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(x: Any) -> list:
    assert isinstance(x, list)
    return x


class CarInfo:
    def __init__(self,
                 header: str = None,
                 image_url: list = None,
                 price: str = None,
                 brand: str = None,
                 model: str = None,
                 exterior_color: str = None,
                 trans_type: str = None):
        if image_url is None:
            # list is mutable
            image_url = []
        self._car_header = from_str(header)
        self._car_image = from_list(image_url)
        self._car_price = from_str(price)
        self._car_brand = from_str(brand)
        self._car_model = from_str(model)
        self._car_exterior_color = from_str(exterior_color)
        self._car_trans_type = from_str(trans_type)

    def to_dict(self) -> dict:
        results = {"header": self._car_header, "image_url": self._car_image, "price": self._car_price,
                   "brand": self._car_brand, "model": self._car_model, "exterior_color": self._car_exterior_color,
                   "trans_type": self._car_trans_type}
        return results

    @property
    def char_header(self):
        return self._car_header

    @char_header.setter
    def char_header(self, value):
        self._car_header = from_str(value)

    @property
    def price(self):
        return self._car_price

    @price.setter
    def price(self, value):
        self._car_price = from_str(value)

    @property
    def brand(self):
        return self._car_brand

    @brand.setter
    def brand(self, value):
        self._car_brand = from_str(value)

    @property
    def model(self):
        return self._car_model

    @model.setter
    def model(self, value):
        self._car_model = from_str(value)

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
