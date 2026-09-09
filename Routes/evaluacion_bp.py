from flask import Blueprint
from Controllers.evaluacionController import evaluacionController


evaluacion_bp = Blueprint("evaluacion_bp", __name__)


@evaluacion_bp.route("/", methods=["GET"])
def show():
    return evaluacionController.show()


@evaluacion_bp.route("/", methods=["POST"])
def add():
    return evaluacionController.add()

