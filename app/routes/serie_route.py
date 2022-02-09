from flask import Blueprint
from app.controllers import serie_controller

bp = Blueprint("series", __name__)

bp.get("/series")(serie_controller.series)
bp.post("/series")(serie_controller.create)
bp.get("/series/<int:id>")(serie_controller.serie_by_id)