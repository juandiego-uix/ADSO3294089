from flask import Blueprint
from Controllers.matriculaController import matriculaController


matricula_bp = Blueprint("matricula_bp", __name__)


@matricula_bp.route("/", methods=["GET"])
def show():
    return matriculaController.show()


@matricula_bp.route("/", methods=["POST"])
def add():
    return matriculaController.add()


@matricula_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return matriculaController.update(item_id)


@matricula_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return matriculaController.delete(item_id)