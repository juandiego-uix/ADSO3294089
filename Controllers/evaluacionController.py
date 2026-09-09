from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Controllers.validation import missing_fields


class evaluacionController:

    @staticmethod
    def show():
        data = evaluacionService.show()
        return jsonify(data), 200

    @staticmethod       
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        
        campos_req = ["nombre", "codigo", "porcentaje", "fecha"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = evaluacionService.add(data)
        return jsonify (x), 201
