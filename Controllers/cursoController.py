from flask import jsonify, request
from Services.cursoService import cursoService
from Controllers.validation import missing_fields


class cursoController:

    @staticmethod
    def show():
        data = cursoService.show()
        return jsonify(data), 200
    
    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400

        campos_req = ["nombre", "codigo", "duracion"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = cursoService.add(data)
        return jsonify (x), 201
