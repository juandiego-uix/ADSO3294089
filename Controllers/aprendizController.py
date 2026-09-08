from flask import jsonify , request
from Services.aprendizService import aprendizService


class aprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200
    
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["fecha_nac" , "per_id"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = aprendizService.add(data)
        return jsonify (x), 201

