from flask import jsonify, request
from Services.cursoService import cursoService
from Controllers.validation import validate_payload


class cursoController:
    @staticmethod
    def show():
        return jsonify(cursoService.show()), 200

    @staticmethod
    def add():
        data, error = cursoController._validate_data()
        if error:
            return error
        return jsonify(cursoService.add(data)), 201

    @staticmethod
    def update(cur_uuid):
        data, error = cursoController._validate_data()
        if error:
            return error
        if not cursoService.update(cur_uuid, data):
            return jsonify({"error": "Curso no encontrado"}), 404
        return jsonify({"mensaje": "Curso actualizado"}), 200

    @staticmethod
    def delete(cur_uuid):
        if not cursoService.delete(cur_uuid):
            return jsonify({"error": "Curso no encontrado"}), 404
        return jsonify({"mensaje": "Curso eliminado"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["nombre", "codigo", "duracion", "costo"],
            integer_fields=["duracion"],
            decimal_fields=["costo"],
            ranges={"costo": (0, None)},
            defaults={"descripcion": None}
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
