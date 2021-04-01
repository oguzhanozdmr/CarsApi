from configparser import ConfigParser

config = ConfigParser()

config['query_header'] = {
    'exterior_color': 'extcolor',
    'brand': 'brand',
    'year': 'year',
    'trans_type': 'trans'
}

config['files'] = {
    'filter_path': './data/car_filters.json'
}

with open('../config.ini', 'w+') as file:
    config.write(file)