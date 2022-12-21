import json

import pymongo
from bson import json_util
from pymongo import MongoClient

from scripts.config.app_configurations import MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_URI
from scripts.logging.application_logging import logger


class MongoUtility:
    def __init__(self):
        self.mongo_client = MongoClient(MONGO_URI)

    def insert_record(self, collection_name, data):
        try:
            mongo_obj = self.mongo_client
            db = mongo_obj[MONGO_DATABASE]
            collection_name = db[collection_name]
            logger.info("Inside the insert record ")
            collection_name.insert_one(data)
            return True
        except Exception as e:
            logger.error(f"Error occurred while inserting the record,'{str(e)}'", exc_info=True)
            return e

    def find_record(self, collection_name):
        try:
            logger.info("Inside the find record")
            mongo_obj = self.mongo_client
            db = mongo_obj[MONGO_DATABASE]
            collection_name = db[collection_name]
            final_json = collection_name.find({},{'_id': 0})
            return final_json
        except Exception as e:
            logger.error(f"Error occurred while lisiting the record,'{str(e)}'", exc_info=True)
            return e

    @staticmethod
    def parse_json(data):
        return json.loads(json_util.dumps(data))
