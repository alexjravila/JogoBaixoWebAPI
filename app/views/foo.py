from flask import request, jsonify
from http import HTTPStatus

def get_all():
    data = ["teste1", "teste2"]

    response = jsonify(data)
    response.status_code = HTTPStatus.OK
    return response

def get_by_name(name):
    data = ["teste1", "teste2"]

    match = [item for item in data if name == item]

    response = jsonify(match)
    response.status_code = HTTPStatus.OK
    return response
