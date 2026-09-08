from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Services.instructorService import instructorService

class instructorController:

    @staticmethod
    def show():
        data = instructorService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["INS_UUID", "INS_ESPECIALIDAD", "INS_PER_ID"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = instructorService.add(data)
        return jsonify (x), 201
