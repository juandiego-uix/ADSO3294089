from flask import Blueprint
from Controllers.materiaEvaluaController import materiaEvaluaController


materia_evalua_bp = Blueprint("materia_evalua_bp", __name__)


@materia_evalua_bp.route("/", methods=["GET"])
def show():
    return materiaEvaluaController.show()


@materia_evalua_bp.route("/", methods=["POST"])
def add():
    return materiaEvaluaController.add()

