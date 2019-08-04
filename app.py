from flask import Flask
from conf import dev_conf
from utils import exception_handler


def create_app():
    from . import db, models, routes, services
    app = Flask(__name__)
    # load config
    app.config.from_object(dev_conf)
    db.init_app(app)
    models.init_app(app)
    services.init_app(app)
    routes.init_app(app)
    exception_handler.init(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
