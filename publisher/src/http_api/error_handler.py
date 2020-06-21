"""
In this file we'll be catching all exception from our application

This file got a logger integration located at urbvan directory
"""
import logging

from flask import jsonify
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import Unauthorized

from src.http_api.exceptions import ApiException
from src.http_api.main import app


LOGGER = logging.getLogger("app_name")


@app.errorhandler(Unauthorized)
@app.errorhandler(HTTPException)
def handle_error(error):
    data = jsonify(
        {
            "code": error.code,
            "name": error.name,
            "description": error.description,
        }  # NOQA
    )
    LOGGER.error(error.description)
    return data, error.code


@app.errorhandler(ApiException)
def handle_api_error(error):
    data = jsonify({"code": error.status_code, "message": error.message})
    LOGGER.error(error.message)
    return data, error.status_code


@app.errorhandler(Exception)
@app.errorhandler(InternalServerError)
def handle_exception_error(error):
    data = jsonify({"code": 500, "name": "Internal Server Error"})
    LOGGER.error(str(error))
    return data, 500
