from flask import request, Blueprint, jsonify
from http import HTTPStatus

app_foo = Blueprint("foo", __name__)

@app_foo.route("", methods=["GET"])
def get_all():
    data = ["teste 1", "teste 2"]

    response = jsonify(data)
    response.status_code = HTTPStatus.OK
    return response
