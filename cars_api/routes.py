# -*- coding: utf-8 -*-
"""
    Cars api routing
"""
from flask import jsonify, request
from cars_api import app, controller

# TODO: swagger will be added


@app.route('/cars/list', methods=['GET'])
def car_list():
    args = request.args
    get_cars = controller.car_list(args)
    return jsonify(get_cars)


@app.route('/', methods=['GET'])
def info():
    return """ <p>/cars/list -> 50 tane araç</p>
               <p>/cars/list?extcolor=black -> Siyah renkli 50 tane araç</p>
               <p>/cars/list?brand=BMW&extcolor=black : Siyah renkli BMW 50 tane araç</p>
               <p>/cars/list?trans=automatic&brand=Ford&year=2018 : Otomatik vites türündeki 2018 yılına ait Ford marka 50  araç. </p>
            """


