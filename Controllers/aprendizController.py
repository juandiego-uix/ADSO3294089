from flask import jsonify
from Services.aprendizService import aprendizService


class aprendizController:

    def show():
        data = aprendizService.show()
        return jsonify(data), 200


