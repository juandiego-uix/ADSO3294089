from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Services.imparteService import imparteService


class imparteController:

    @staticmethod
    def show():
        data = imparteService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["IMP_UUID", "IMP_ROL", "IMP_FECHA", "IMP_FECHA_ASIGNACION", "IMP_CUR_ID", "IMP_INS_ID"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = imparteService.add(data)
        return jsonify (x), 201
