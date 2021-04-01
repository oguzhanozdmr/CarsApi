from cars_api import app, CarFilters
from os.path import isfile
from configparser import ConfigParser


def create_json():
    car_filters = CarFilters()
    car_filters.save_filter()


def main():
    if isfile('./config.ini'):
        parser = ConfigParser()
        parser.read('config.ini')

        json_path = parser.get('files', 'filter_path')
        if isfile(json_path):
            app.run(debug=True)
        else:
            create_json()
            print("json have been created. Run it again")
    else:
        print("Config.ini is missing")


if __name__ == '__main__':
    main()
