from flask import Flask

from app.routes.serie_route import bp as bp_series

def init_app(app: Flask):

    app.register_blueprint(bp_series)