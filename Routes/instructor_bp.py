from flask import Blueprint
from Controllers.instructorController import instructorController


instructor_bp = Blueprint("instructor_bp", __name__)


@instructor_bp.route("/", methods=["GET"])
def show():
    return instructorController.show()


@instructor_bp.route("/", methods=["POST"])
def add():
    return instructorController.add()


@instructor_bp.route("/<int:item_id>", methods=["PUT"])
def update(item_id):
    return instructorController.update(item_id)


@instructor_bp.route("/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    return instructorController.delete(item_id)