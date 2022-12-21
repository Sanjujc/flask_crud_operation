import pymongo
from pymongo import MongoClient

from scripts.config.app_configurations import MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_URI
from scripts.logging.application_logging import logger


class MongoUtility:
    def __init__(self):
        connect = pymongo.MongoClient('mongodb://loclhost:27017/')
        self.db = connect['flask_crud']
        self.collection_name = self.db['user_management']

    def insert_record(self, collection_name, data):
        try:
            logger.info("Inside the insert record ")
            user_management = self.collection_name
            post_id = user_management.insert_one(data)
            print(post_id)
            return post_id
        except Exception as e:
            logger.error("Error occurred while inserting the record")
            return e
