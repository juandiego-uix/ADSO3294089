from flask import jsonify, request
from Services.PersonaService import PersonaService
from Controllers.validation import missing_fields


class PersonaController:

    @staticmethod
    def show():
        data = PersonaService.show()
        return jsonify(data), 200
    
    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if not isinstance(data, dict):
            return jsonify({"error": "json invalido"}), 400
        
        campos_req = ["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido", "documento"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"faltan parametros: {faltantes}"}), 400
        
        x = PersonaService.add(data)
        return jsonify (x), 201


