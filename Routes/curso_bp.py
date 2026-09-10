from flask import Blueprint
from Controllers.cursoController import cursoController

curso_bp = Blueprint('curso_bp', __name__)

@curso_bp.route('/', methods=['GET'])
def home():
    return cursoController.show()

@curso_bp.route('/', methods=['POST'])
def add():
    return cursoController.add()

@curso_bp.route('/<string:cur_uuid>', methods=['PUT'])
def update(cur_uuid):
    return cursoController.update(cur_uuid)

@curso_bp.route('/<string:cur_uuid>', methods=['DELETE'])
def delete(cur_uuid):
    return cursoController.delete(cur_uuid)
