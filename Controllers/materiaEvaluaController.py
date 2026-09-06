from flask import jsonify
from Services.MateriaEvaluaService import MateriaEvaluaService


class materiaEvaluaController:

    @staticmethod
    def show():
        data = MateriaEvaluaService.show()
        return jsonify(data), 200