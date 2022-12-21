from flask import Flask, request, Response, Blueprint

from scripts.config.app_constants import Status
from scripts.core.Handler.user_management_handler import UserManagement
from scripts.logging.application_logging import logger

user_service = Blueprint('user_service', __name__)


@user_service.route('/register_user', methods=['GET', 'POST'])
def register_user():
    try:
        if request.method == 'POST':
            logger.info("Inside the register user template")
            data = request.json
            final_json = UserManagement().register_user(data)
            return final_json
        else:
            logger.info("The given request is a get method")
            return Response('URL Not Found', status=404)
    except Exception as e:
        logger.error(f"Error occurred while inserting the user:{str(e)}", exc_info=True)
        return Status.error_occurred


@user_service.get('/list_user')
def list_user():
    try:
        logger.info("Inside the list user service")
        final_json = UserManagement().find_all_user()
        return final_json
    except Exception as e:
        logger.error(f"Error occurred while inserting the user:{str(e)}", exc_info=True)
        return Status.error_occurred


@user_service.get('/list_user_by_specific')
def list_user_by_specific():
    try:
        logger.info("Inside the list user specific service")
        request_data = request.json
        print(request_data)
        final_json = UserManagement().find_user_by_specific(request_data)
        return final_json
    except Exception as e:
        logger.error(f"Error occurred while inserting the user:{str(e)}", exc_info=True)
        return Status.error_occurred
