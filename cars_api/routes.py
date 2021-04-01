from cars_api import app, get_json, controller
from flask import jsonify, request


@app.route('/cars/list', methods=['GET'])
def car_list():
    args = request.args
    controller.car_list(args)
    get = get_json.GetJson()
    return jsonify(get.get_requests())
