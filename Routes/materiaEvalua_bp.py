from flask import Blueprint
from Controllers.materiaEvaluaController import materiaEvaluaController

materia_evalua_bp = Blueprint('materia_evalua_bp', __name__)

@materia_evalua_bp.route('/', methods=['GET'])
def home():
    return materiaEvaluaController.show()

@materia_evalua_bp.route('/', methods=['POST'])
def add():
    return materiaEvaluaController.add()

@materia_evalua_bp.route('/<string:mate_uuid>', methods=['PUT'])
def update(mate_uuid):
    return materiaEvaluaController.update(mate_uuid)

@materia_evalua_bp.route('/<string:mate_uuid>', methods=['DELETE'])
def delete(mate_uuid):
    return materiaEvaluaController.delete(mate_uuid)
