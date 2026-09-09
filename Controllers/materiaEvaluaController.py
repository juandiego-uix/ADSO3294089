from flask import jsonify, request
from Services.MateriaEvaluaService import materia_evaluaService
from Services.evaluacionService import evaluacionService


class materiaEvaluaController:

    @staticmethod
    def show():
        data = materia_evaluaService.show()
        return jsonify(data), 200 
    
    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["nota", "eva_id", "mat_id"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = materia_evaluaService.add(data)
        return jsonify (x), 201
