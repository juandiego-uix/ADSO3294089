from flask import jsonify, request
from Services.personaService import personaService
from Controllers.validation import validate_payload


class personaController:
    @staticmethod
    def show():
        return jsonify(personaService.show()), 200

    @staticmethod
    def add():
        data, error = personaController._validate_data()
        if error:
            return error
        return jsonify(personaService.add(data)), 201

    @staticmethod
    def update(per_uuid):
        data, error = personaController._validate_data()
        if error:
            return error
        if not personaService.update(per_uuid, data):
            return jsonify({"error": "Persona no encontrada"}), 404
        return jsonify({"mensaje": "Persona actualizada"}), 200

    @staticmethod
    def delete(per_uuid):
        if not personaService.delete(per_uuid):
            return jsonify({"error": "Persona no encontrada"}), 404
        return jsonify({"mensaje": "Persona eliminada"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["pri_nombre", "pri_apellido", "documento"],
            defaults={"seg_nombre": None, "seg_apellido": None}
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
