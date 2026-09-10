from flask import jsonify, request
from Services.matriculaService import matriculaService
from Controllers.validation import validate_payload


class matriculaController:
    @staticmethod
    def show():
        return jsonify(matriculaService.show()), 200

    @staticmethod
    def add():
        data, error = matriculaController._validate_data()
        if error:
            return error
        return jsonify(matriculaService.add(data)), 201

    @staticmethod
    def update(mat_uuid):
        data, error = matriculaController._validate_data()
        if error:
            return error
        if not matriculaService.update(mat_uuid, data):
            return jsonify({"error": "Matricula no encontrada"}), 404
        return jsonify({"mensaje": "Matricula actualizada"}), 200

    @staticmethod
    def delete(mat_uuid):
        if not matriculaService.delete(mat_uuid):
            return jsonify({"error": "Matricula no encontrada"}), 404
        return jsonify({"mensaje": "Matricula eliminada"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["fecha", "estado", "per_id", "cur_id"],
            integer_fields=["per_id", "cur_id"],
            date_fields=["fecha"]
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
