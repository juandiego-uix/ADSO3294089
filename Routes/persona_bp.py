from flask import Blueprint
from Controllers.personaController import PersonaController


persona_bp = Blueprint("persona_bp", __name__)


@persona_bp.route("/", methods=["GET"])
def show():
    return PersonaController.show()


@persona_bp.route("/", methods=["POST"])
def add():
    return PersonaController.add()

@persona_bp.route("/", methods=["DELETE"])
def delete():
    return PersonaController.add()