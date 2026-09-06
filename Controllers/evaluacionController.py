from flask import jsonify
from Services.evaluacionService import evaluacionService


class evaluacionController:

    @staticmethod
    def show():
        data = evaluacionService.show()
        return jsonify(data), 200