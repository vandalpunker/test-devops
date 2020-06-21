import logging

from flask import request

from src.http_api.main import app

LOGGER = logging.getLogger("app_name")


@app.before_request
def logger():
    req = request
    LOGGER.info(f"{req}: {req.base_url} - {req.method} - {req.data}")
