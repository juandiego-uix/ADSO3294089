from flask import jsonify
from Services.instructorService import instructorService


class instructorController:

    @staticmethod
    def show():
        data = instructorService.show()
        return jsonify(data), 200