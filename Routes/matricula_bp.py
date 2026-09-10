from flask import Blueprint
from Controllers.matriculaController import matriculaController

matricula_bp = Blueprint('matricula_bp', __name__)

@matricula_bp.route('/', methods=['GET'])
def home():
    return matriculaController.show()

@matricula_bp.route('/', methods=['POST'])
def add():
    return matriculaController.add()

@matricula_bp.route('/<string:mat_uuid>', methods=['PUT'])
def update(mat_uuid):
    return matriculaController.update(mat_uuid)

@matricula_bp.route('/<string:mat_uuid>', methods=['DELETE'])
def delete(mat_uuid):
    return matriculaController.delete(mat_uuid)
