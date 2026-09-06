from flask import Blueprint
from Controllers.personaController import PersonaController


persona_bp = Blueprint("persona_bp", __name__)


@persona_bp.route("/", methods=["GET"])
def show():
    return PersonaController.show()


@persona_bp.route("/", methods=["POST"])
def add():
    return PersonaController.add()


@persona_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return PersonaController.update(item_id)


@persona_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return PersonaController.delete(item_id)