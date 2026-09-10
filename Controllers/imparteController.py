from flask import jsonify, request
from Services.imparteService import imparteService
from Controllers.validation import validate_payload


class imparteController:
    @staticmethod
    def show():
        return jsonify(imparteService.show()), 200

    @staticmethod
    def add():
        data, error = imparteController._validate_data()
        if error:
            return error
        return jsonify(imparteService.add(data)), 201

    @staticmethod
    def update(imp_uuid):
        data, error = imparteController._validate_data()
        if error:
            return error
        if not imparteService.update(imp_uuid, data):
            return jsonify({"error": "Asignacion no encontrada"}), 404
        return jsonify({"mensaje": "Asignacion actualizada"}), 200

    @staticmethod
    def delete(imp_uuid):
        if not imparteService.delete(imp_uuid):
            return jsonify({"error": "Asignacion no encontrada"}), 404
        return jsonify({"mensaje": "Asignacion eliminada"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["rol", "fecha", "fecha_asignacion", "cur_id", "ins_id"],
            integer_fields=["cur_id", "ins_id"],
            date_fields=["fecha", "fecha_asignacion"]
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
