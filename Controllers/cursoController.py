from flask import jsonify
from Services.cursoService import cursoService


class cursoController:

    @staticmethod
    def show():
        data = cursoService.show()
        return jsonify(data), 200