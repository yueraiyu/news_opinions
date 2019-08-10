from http.client import HTTPException
from flask import render_template


def init(app):
    @app.errorhandler(404)
    def error_404(e):
        code = 404
        msg = "request error, please check the request parameters or url"
        return render_template('error/error.html', code=code, msg=msg)

    @app.errorhandler(Exception)
    def server_error_handler(e):
        code = 500
        msg = "server error, try again later "
        if isinstance(e, HTTPException):
            msg, code = e.desciption, e.code
        return render_template('error/error.html', code=code, msg=msg)
