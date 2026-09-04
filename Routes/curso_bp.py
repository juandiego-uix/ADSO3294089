from flask import Blueprint
from Controllers.cursoController import cursoController


curso_bp = Blueprint("curso_bp", __name__)


@curso_bp.route("/", methods=["GET"])
def show():
    return cursoController.show()


@curso_bp.route("/", methods=["POST"])
def add():
    return cursoController.add()


@curso_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return cursoController.update(item_id)


@curso_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return cursoController.delete(item_id)