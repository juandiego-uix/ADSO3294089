from flask import jsonify, request
from Services.instructorService import instructorService
from Controllers.validation import validate_payload


class instructorController:
    @staticmethod
    def show():
        return jsonify(instructorService.show()), 200

    @staticmethod
    def add():
        data, error = instructorController._validate_data()
        if error:
            return error
        return jsonify(instructorService.add(data)), 201

    @staticmethod
    def update(ins_uuid):
        data, error = instructorController._validate_data()
        if error:
            return error
        if not instructorService.update(ins_uuid, data):
            return jsonify({"error": "Instructor no encontrado"}), 404
        return jsonify({"mensaje": "Instructor actualizado"}), 200

    @staticmethod
    def delete(ins_uuid):
        if not instructorService.delete(ins_uuid):
            return jsonify({"error": "Instructor no encontrado"}), 404
        return jsonify({"mensaje": "Instructor eliminado"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["especialidad", "per_id"],
            integer_fields=["per_id"]
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
