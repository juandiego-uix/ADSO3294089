from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Services.imparteService import imparteService
from Controllers.validation import missing_fields


class imparteController:

    @staticmethod
    def show():
        data = imparteService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        campos_req = ["rol", "fecha_asignacion"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = imparteService.add(data)
        return jsonify (x), 201
