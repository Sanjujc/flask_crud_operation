import configparser

config = configparser.ConfigParser()
config.read('conf/application.conf')

"""
log_level
"""
LOG_LEVEL = config.get('LOG', 'log_level')
LOG_BASEPATH = config.get('LOG', 'base_path')
LOG_FILE_NAME = LOG_BASEPATH + config.get('LOG', 'file_name')
LOG_HANDLERS = config.get('LOG', 'handlers')
LOGGER_NAME = config.get('LOG', 'logger_name')

"""
mongo_db
"""
MONGO_HOST = config.get('MONGO', 'mongo_host')
MONGO_PORT = config.get('MONGO', 'mongo_port')
MONGO_DATABASE = config.get('MONGO', 'database')
MONGO_URI = config.get('MONGO', 'connection_uri')
