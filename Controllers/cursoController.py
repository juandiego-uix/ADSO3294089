from flask import jsonify, request
from Services.cursoService import cursoService


class cursoController:

    @staticmethod
    def show():
        data = cursoService.show()
        return jsonify(data), 200
    
    def add():
        date = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["fecha_nac" , "per_id"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = cursoService.add(data)
        return jsonify (x), 201
