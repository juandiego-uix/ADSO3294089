from flask import jsonify
from Services.MateriaEvaluaService import materia_evaluaService


class materiaEvaluaController:

    @staticmethod
    def show():
        data = MateriaEvaluaService.show()
        return jsonify(data), 200