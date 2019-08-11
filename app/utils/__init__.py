# utils init
from logging.config import dictConfig


def init_app(app):
    logger_config = app.config.get("LOGGER_DICT")
    dictConfig(logger_config)