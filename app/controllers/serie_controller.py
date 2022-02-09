from flask import jsonify, request
from http import HTTPStatus
from app.models.serie_model import Serie
from psycopg2.errors import UniqueViolation

def series():

    series = Serie.read_series()

    series_list = Serie.serealiaze_serie(series)

    return jsonify(series_list), HTTPStatus.OK


def serie_by_id(id):
    
    serie = Serie.get_specific_serie(id)

    if not serie:
        return jsonify({}), HTTPStatus.NOT_FOUND

    seriealized_serie = Serie.serealiaze_serie(serie)

    return jsonify(seriealized_serie), HTTPStatus.OK


def create():
    data = request.get_json()

    serie = Serie(**data)

    try:
        inserted_serie = serie.create_serie()

    except UniqueViolation as e:
        return jsonify({"msg": e.args}), HTTPStatus.UNPROCESSABLE_ENTITY

    inserted_serie = Serie.serealiaze_serie(inserted_serie)

    return jsonify(inserted_serie), HTTPStatus.CREATED