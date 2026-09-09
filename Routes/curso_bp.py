from flask import Blueprint
from Controllers.cursoController import cursoController


curso_bp = Blueprint("curso_bp", __name__)


@curso_bp.route("/", methods=["GET"])
def show():
    return cursoController.show()


@curso_bp.route("/", methods=["POST"])
def add():
    return cursoController.add()

@curso_bp.route("/", methods=["DELETE"])
def delete():
    return cursoController.add()
