import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from pyltp import Segmentor, Postagger, NamedEntityRecognizer, Parser
from config import Config

# Flask-SQLAlchemy plugin
db = SQLAlchemy()

# nlp 模型
basepath = os.path.abspath('.')
sys.path.append(basepath)
path = os.getcwd()

LTP_DATA_DIR = os.path.join(basepath, "app", "models")  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
similar_word_path = os.path.join(basepath, "app", "utils", "similar_word", "similar_word_to_say.txt")

# Postagger
postagger = Postagger()
postagger.load(pos_model_path)

# NamedEntityRecognizer
recognizer = NamedEntityRecognizer()
recognizer.load(ner_model_path)

# Parser
parser = Parser()
parser.load(par_model_path)

# Segmentor
segmentor = Segmentor()
segmentor.load(cws_model_path)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Init log
    logger_config = app.config.get("LOGGER_DICT")
    dictConfig(logger_config)

    # Enable CORS
    CORS(app, supports_credentials=True)
    # Init Flask-SQLAlchemy
    db.init_app(app)

    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app.database import models