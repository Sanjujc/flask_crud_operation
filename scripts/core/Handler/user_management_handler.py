from scripts.config.app_constants import CollectionName, Status
from scripts.logging.application_logging import logger
from scripts.utilities.mongo_utility import MongoUtility


class UserManagement:
    def __init__(self):
       self.collection_name = CollectionName.user_management


    def register_user(self,request_data):
        try:
            logger.info("Inside the register user handler")
            if request_data:
                MongoUtility().insert_record(collection_name=self.collection_name, data=request_data)
                logger.info("Inserting the data")
                final_response = {
                    'status': Status.executed,
                    'message': 'Successfully Inserted'
                }
                return final_response
        except Exception as e:
            logger.error(f"Error occurred while registering the user:'{str(e)}'"
                         , exc_info=True)
            return e

    def find_all_user(self):
        try:
            logger.error("Inside the listing all user handler")
            record = MongoUtility().find_record(self.collection_name)
            final_json = MongoUtility().parse_json(record)
            return final_json
        except Exception as e:
            logger.error(f"Error occurred while listing all the user details:{str(e)}",exc_info=True)
            return False
