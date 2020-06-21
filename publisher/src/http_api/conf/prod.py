from .base import BaseConfig


class Config(BaseConfig):
    """
    Development environment configuration
    """

    TESTING = False
    DEBUG = False
