# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    return aprendizController.show()


@apr_bp.route('/', methods=['POST'])
def add():
    return aprendizController.add()


@apr_bp.route('/<string:apr_uuid>', methods=['PUT'])
def update(apr_uuid):
    return aprendizController.update(apr_uuid)


@apr_bp.route('/<string:apr_uuid>', methods=['DELETE'])
def delete(apr_uuid):
    return aprendizController.delete(apr_uuid)
