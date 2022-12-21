from scripts.config.app_constants import CollectionName
from scripts.logging.application_logging import logger
from scripts.utilities.mongo_utility import MongoUtility


class UserManagement:
    def __init__(self):
        pass

    @staticmethod
    def register_user(request_data):
        try:
            logger.info("Inside the register user handler")
            user_management_collection = CollectionName.user_management
            final_data = {
                'name': 'Sanju'
            }
            MongoUtility().insert_record(user_management_collection, data=final_data)
            return True
        except Exception as e:
            logger.error(f"Error occured while registering the user:'{str(e)}'"
                         , exc_info=True)
            return e
