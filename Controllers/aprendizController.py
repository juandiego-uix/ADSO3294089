from flask import jsonify , request
from Services.aprendizService import aprendizService
from Controllers.validation import missing_fields


class aprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        campos_req = ["fecha_nac" , "per_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = aprendizService.add(data)
        return jsonify (x), 201

