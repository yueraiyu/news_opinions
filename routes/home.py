from flask import render_template


def init(app):
    logger = app.logger

    @app.route('/')
    def index():
        return render_template('index.html', name="yeay")

