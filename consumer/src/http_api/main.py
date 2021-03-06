import logging
from environs import Env
from flask import Flask

from src.http_api.apps.consumer.routes import consumer

app = Flask(__name__)

from src.http_api.error_handler import *  # NOQA
from src.http_api.middlewares import *  # NOQA


def create_app():
    env = Env()

    # Get flask configuration class from environment variable
    conf = env("FLASK_CONFIG")

    # App configuration
    app.config.from_object(conf)

    # Routes register
    app.register_blueprint(consumer)

    gunicorn_logger = logging.getLogger('gunicorn.debug')
    app.logger.handlers.extend(gunicorn_logger.handlers)
    app.logger.setLevel(logging.DEBUG)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
