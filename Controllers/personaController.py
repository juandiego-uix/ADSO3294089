from flask import jsonify
from Services.PersonaService import PersonaService


class PersonaController:

    def show():
        data = PersonaService.show()
        return jsonify(data), 200


