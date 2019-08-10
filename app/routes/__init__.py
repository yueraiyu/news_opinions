# routes
from . import home


def init_app(app):
    logger = app.logger
    home.init(app)
    logger.info("%s init routes", __name__)

