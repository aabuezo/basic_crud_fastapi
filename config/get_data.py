from configparser import ConfigParser


config = ConfigParser()
config.read("config/config.ini")


data = {
    'host': config.get('SQL', 'host'),
    'database': config.get('SQL', 'database'),
    'user': config.get('SQL', 'user'),
    'password': config.get('SQL', 'password')
}


def get_db_data():
    return data
