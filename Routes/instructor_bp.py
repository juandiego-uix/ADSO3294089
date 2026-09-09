from flask import Blueprint
from Controllers.instructorController import instructorController


instructor_bp = Blueprint("instructor_bp", __name__)


@instructor_bp.route("/", methods=["GET"])
def show():
    return instructorController.show()


@instructor_bp.route("/", methods=["POST"])
def add():
    return instructorController.add()

