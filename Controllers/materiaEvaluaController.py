from flask import jsonify, request
from Services.MateriaEvaluaService import materiaEvaluaService
from Controllers.validation import validate_payload


class materiaEvaluaController:
    @staticmethod
    def show():
        return jsonify(materiaEvaluaService.show()), 200

    @staticmethod
    def add():
        data, error = materiaEvaluaController._validate_data()
        if error:
            return error
        return jsonify(materiaEvaluaService.add(data)), 201

    @staticmethod
    def update(mate_uuid):
        data, error = materiaEvaluaController._validate_data()
        if error:
            return error
        if not materiaEvaluaService.update(mate_uuid, data):
            return jsonify({"error": "Nota no encontrada"}), 404
        return jsonify({"mensaje": "Nota actualizada"}), 200

    @staticmethod
    def delete(mate_uuid):
        if not materiaEvaluaService.delete(mate_uuid):
            return jsonify({"error": "Nota no encontrada"}), 404
        return jsonify({"mensaje": "Nota eliminada"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["nota", "eva_id", "mat_id"],
            integer_fields=["eva_id", "mat_id"],
            decimal_fields=["nota"],
            ranges={"nota": (0, 5)}
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
