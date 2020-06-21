from environs import Env

env = Env()


class BaseConfig:
    """
    FLASK configuration

    Please be sure to add your .env file to your project
    All envs marked with default are optional
    """

    TESTING = env("TESTING", default=False)
    DEBUG = env("DEBUG", default=False)
    SECRET_KEY = env("SECRET_KEY")

    # YOUR STUFF
