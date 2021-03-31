from configparser import ConfigParser

config = ConfigParser()

config['files'] = {
    'filter_path': './data/car_filters.json'
}

with open('./config.ini', 'w+') as file:
    config.write(file)