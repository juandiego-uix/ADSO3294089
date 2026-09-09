from flask import Blueprint
from Controllers.matriculaController import matriculaController


matricula_bp = Blueprint("matricula_bp", __name__)


@matricula_bp.route("/", methods=["GET"])
def show():
    return matriculaController.show()


@matricula_bp.route("/", methods=["POST"])
def add():
    return matriculaController.add()

