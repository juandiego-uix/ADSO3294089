from flask import Blueprint
from Controllers.personaController import personaController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'])
def home():
    return personaController.show()

@persona_bp.route('/', methods=['POST'])
def add():
    return personaController.add()

@persona_bp.route('/<string:per_uuid>', methods=['PUT'])
def update(per_uuid):
    return personaController.update(per_uuid)

@persona_bp.route('/<string:per_uuid>', methods=['DELETE'])
def delete(per_uuid):
    return personaController.delete(per_uuid)
