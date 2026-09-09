from flask import jsonify, request
from Services.evaluacionService import evaluacionService


class evaluacionController:

    @staticmethod
    def show():
        data = evaluacionService.show()
        return jsonify(data), 200

    @staticmethod       
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        
        campos_req = ["nombre", "codigo", "porcentaje", "fecha"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = evaluacionService.add(data)
        return jsonify (x), 201
