from flask import Flask, request, Response, Blueprint

from scripts.core.Handler.user_management_handler import UserManagement
from scripts.logging.application_logging import logger

user_service = Blueprint('user_service', __name__)


@user_service.route('/register_user')
def register_user():
    try:
        logger.info("Inside the register user template")
        data = request.data
        final_json = UserManagement().register_user(data)
        return Response(status=200)
    except Exception as e:
        print(False)