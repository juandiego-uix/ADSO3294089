from flask import Blueprint
from Controllers.personaController import personaController


persona_bp = Blueprint("persona_bp", __name__)


@persona_bp.route("/", methods=["GET"])
def show():
    return personaController.show()


@persona_bp.route("/", methods=["POST"])
def add():
    return personaController.add()


@persona_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return personaController.update(item_id)


@persona_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return personaController.delete(item_id)