from flask import jsonify
from Services.imparteService import imparteService


class imparteController:

    @staticmethod
    def show():
        data = imparteService.show()
        return jsonify(data), 200