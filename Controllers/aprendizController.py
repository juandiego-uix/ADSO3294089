from flask import jsonify , request
from Services.aprendizService import aprendizService
from Controllers.validation import validate_payload


class aprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    @staticmethod
    def add():
        data, error = aprendizController._validate_data()
        if error:
            return error
        aprendiz = aprendizService.add(data)
        return jsonify(aprendiz), 201

    @staticmethod
    def update(apr_uuid):
        data, error = aprendizController._validate_data()
        if error:
            return error

        actualizado = aprendizService.update(apr_uuid, data)
        if not actualizado:
            return jsonify({"error": "Aprendiz no encontrado"}), 404
        return jsonify({"mensaje": "Aprendiz actualizado"}), 200

    @staticmethod
    def delete(apr_uuid):
        eliminado = aprendizService.delete(apr_uuid)
        if not eliminado:
            return jsonify({"error": "Aprendiz no encontrado"}), 404
        return jsonify({"mensaje": "Aprendiz eliminado"}), 200

    @staticmethod
    def _validate_data():
        data = request.get_json(silent=True)
        data, error = validate_payload(
            data,
            required=["fecha_nac", "per_id"],
            integer_fields=["per_id"],
            date_fields=["fecha_nac"]
        )
        if error:
            return None, (jsonify({"error": error}), 400)
        return data, None
