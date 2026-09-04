from flask import Blueprint
from Controllers.materiaEvaluaController import materiaEvaluaController


materia_evalua_bp = Blueprint("materia_evalua_bp", __name__)


@materia_evalua_bp.route("/", methods=["GET"])
def show():
    return materiaEvaluaController.show()


@materia_evalua_bp.route("/", methods=["POST"])
def add():
    return materiaEvaluaController.add()


@materia_evalua_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return materiaEvaluaController.update(item_id)


@materia_evalua_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return materiaEvaluaController.delete(item_id)