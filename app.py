from flask import Flask

from scripts.core.Service.user_management_service import user_service

app = Flask(__name__)

app.register_blueprint(user_service)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
