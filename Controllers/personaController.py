from flask import jsonify, request
from Services.PersonaService import PersonaService


class PersonaController:

    @staticmethod
    def show():
        data = PersonaService.show()
        return jsonify(data), 200
    
    @staticmethod
    def add():
        data = request.get_json(silent = True)
        if data is None:
            return jsonify({"error : json invalido"}), 400
        
        campos_req = ["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido", "documento"]
        faltantes = [w for w in campos_req if w not in data]
        if len(faltantes):
            return jsonify({"mensaje" :f"faltan parametros{faltantes}"}),400
        
        x = PersonaService.add(data)
        return jsonify (x), 201


