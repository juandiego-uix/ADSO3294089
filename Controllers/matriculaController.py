from flask import jsonify
from Services.matriculaService import matriculaService


class matriculaController:

    @staticmethod
    def show():
        data = matriculaService.show()
        return jsonify(data), 200