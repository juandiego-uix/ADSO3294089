from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Services.matriculaService import matriculaService


class matriculaController:

    @staticmethod
    def show():
        data = matriculaService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["MAT_UUID", "MAT_FECHA", "MAT_ESTADO", "MAT_PER_ID", "MAT_CUR_ID"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
            
        x = matriculaService.add(data)
        return jsonify (x), 201
    