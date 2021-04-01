from configparser import ConfigParser

config = ConfigParser()

config['header_to_cars_api'] = {
    'exterior_color': 'clrId',
    'brand': 'mkId',
    'year': 'yrId',
    'trans_type': 'transTypeId'
}

config['request_header'] = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, '
                  'like Gecko) Version/13.1.3 Safari/605.1.15',
    'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/ocsp-request'
}

config['query_header'] = {
    'exterior_color': 'extcolor',
    'brand': 'brand',
    'year': 'year',
    'trans_type': 'trans'
}

config['files'] = {
    'filter_path': './data/car_filters.json'
}

with open('cars_config_2.ini', 'w+') as file:
    config.write(file)
