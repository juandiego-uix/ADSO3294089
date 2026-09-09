from flask import Blueprint
from Controllers.imparteController import imparteController


imparte_bp = Blueprint("imparte_bp", __name__)


@imparte_bp.route("/", methods=["GET"])
def show():
    return imparteController.show()


@imparte_bp.route("/", methods=["POST"])
def add():
    return imparteController.add()


@imparte_bp.route("/", methods=["DELETE"])
def delete():
    return imparteController.add()