from flask import Blueprint
from Controllers.instructorController import instructorController

instructor_bp = Blueprint('instructor_bp', __name__)

@instructor_bp.route('/', methods=['GET'])
def home():
    return instructorController.show()

@instructor_bp.route('/', methods=['POST'])
def add():
    return instructorController.add()

@instructor_bp.route('/<string:ins_uuid>', methods=['PUT'])
def update(ins_uuid):
    return instructorController.update(ins_uuid)

@instructor_bp.route('/<string:ins_uuid>', methods=['DELETE'])
def delete(ins_uuid):
    return instructorController.delete(ins_uuid)
