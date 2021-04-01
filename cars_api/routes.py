from cars_api import app, get_json
from flask import jsonify, request
from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')

color_query = config['query_header']['exterior_color']
brand_query = config['query_header']['brand']
year_query = config['query_header']['year']
request_query = config['query_header']['trans_type']

@app.route('/cars/list', methods=['GET'])
def car_list():
    get = get_json.GetJson()
    args = request.args
    if color_query in args:
        exterior_color = args.get(color_query)
        print(exterior_color)
    if brand_query in args:
        brand = args.get(brand_query)
    if year_query in args:
        year = args.get(year_query)
    if request_query in request.args:
        trans_type = request.args.get(request_query)

    return jsonify(get.get_requests())

