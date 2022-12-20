from flask import Flask, request, Response, Blueprint

user_service = Blueprint('user_service', __name__)


@user_service.route('/register_user')
def register_user():
    try:
        data = request.data
        return Response(data)
    except Exception as e:
        print(False)
