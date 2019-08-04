# db


def init_app(app):
    logger = app.logger
    logger.info("%s init db", __name__)
