from flask import Blueprint
from Controllers.evaluacionController import evaluacionController


evaluacion_bp = Blueprint("evaluacion_bp", __name__)


@evaluacion_bp.route("/", methods=["GET"])
def show():
    return evaluacionController.show()


@evaluacion_bp.route("/", methods=["POST"])
def add():
    return evaluacionController.add()


@evaluacion_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return evaluacionController.update(item_id)


@evaluacion_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return evaluacionController.delete(item_id)