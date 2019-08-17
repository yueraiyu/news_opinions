from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from config import Config


# Flask-SQLAlchemy plugin
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Init log
    logger_config = app.config.get("LOGGER_DICT")
    dictConfig(logger_config)

    # Enable CORS
    CORS(app)
    # Init Flask-SQLAlchemy
    db.init_app(app)

    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app.database import models