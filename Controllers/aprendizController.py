from flask import jsonify
from Services.aprendizService import aprendizService


class aprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200


