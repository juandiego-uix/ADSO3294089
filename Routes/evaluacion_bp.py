from flask import Blueprint
from Controllers.evaluacionController import evaluacionController

evaluacion_bp = Blueprint('evaluacion_bp', __name__)

@evaluacion_bp.route('/', methods=['GET'])
def home():
    return evaluacionController.show()

@evaluacion_bp.route('/', methods=['POST'])
def add():
    return evaluacionController.add()

@evaluacion_bp.route('/<string:eva_uuid>', methods=['PUT'])
def update(eva_uuid):
    return evaluacionController.update(eva_uuid)

@evaluacion_bp.route('/<string:eva_uuid>', methods=['DELETE'])
def delete(eva_uuid):
    return evaluacionController.delete(eva_uuid)
