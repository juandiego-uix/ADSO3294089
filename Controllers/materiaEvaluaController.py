from flask import jsonify, request
from Services.MateriaEvaluaService import materia_evaluaService
from Controllers.validation import missing_fields
from Services.evaluacionService import evaluacionService


class materiaEvaluaController:

    @staticmethod
    def show():
        data = materia_evaluaService.show()
        return jsonify(data), 200 
    
    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        campos_req = ["nota", "mat_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = materia_evaluaService.add(data)
        return jsonify (x), 201
