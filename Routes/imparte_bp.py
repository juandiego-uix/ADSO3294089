from flask import Blueprint
from Controllers.imparteController import imparteController

imparte_bp = Blueprint('imparte_bp', __name__)

@imparte_bp.route('/', methods=['GET'])
def home():
    return imparteController.show()

@imparte_bp.route('/', methods=['POST'])
def add():
    return imparteController.add()

@imparte_bp.route('/<string:imp_uuid>', methods=['PUT'])
def update(imp_uuid):
    return imparteController.update(imp_uuid)

@imparte_bp.route('/<string:imp_uuid>', methods=['DELETE'])
def delete(imp_uuid):
    return imparteController.delete(imp_uuid)
