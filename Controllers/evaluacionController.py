from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Controllers.validation import validate_payload


class evaluacionController:
    @staticmethod
    def show():
        return jsonify(evaluacionService.show()), 200

    @staticmethod
    def add():
        data, error = evaluacionController._validate_data()
        if error:
            return error
        return jsonify(evaluacionService.add(data)), 201

    @staticmethod
    def update(eva_uuid):
        data, error = evaluacionController._validate_data()
        if error:
            return error
        if not evaluacionService.update(eva_uuid, data):
            return jsonify({"error": "Evaluacion no encontrada"}), 404
        return jsonify({"mensaje": "Evaluacion actualizada"}), 200

    @staticmethod
    def delete(eva_uuid):
        if not evaluacionService.delete(eva_uuid):
            return jsonify({"error": "Evaluacion no encontrada"}), 404
        return jsonify({"mensaje": "Evaluacion eliminada"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["nombre", "codigo", "porcentaje", "fecha"],
            decimal_fields=["porcentaje"],
            date_fields=["fecha"],
            ranges={"porcentaje": (0, 100)}
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
