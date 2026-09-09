from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Services.matriculaService import matriculaService
from Controllers.validation import missing_fields


class matriculaController:

    @staticmethod
    def show():
        data = matriculaService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        campos_req = ["estado", "fecha_inscripcion"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
            
        x = matriculaService.add(data)
        return jsonify (x), 201
    