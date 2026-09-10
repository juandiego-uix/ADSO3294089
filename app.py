from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from flask_mysqldb import MySQL
from Config import Config
from Routes import loadRoutes

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
mysql = MySQL(app)

app.mysql = mysql
loadRoutes(app)


@app.get("/")
def home():
	return jsonify({
		"mensaje": "API ADSO4089 funcionando",
		"rutas": {
			"aprendices": "/aprendices/",
			"personas": "/personas/",
			"instructores": "/instructores/",
			"cursos": "/cursos/",
			"evaluaciones": "/evaluaciones/",
			"matriculas": "/matriculas/",
			"imparte": "/imparte/",
			"materia_evalua": "/materia-evalua/"
		}
	}), 200


@app.errorhandler(HTTPException)
def handle_http_error(error):
	return jsonify({"error": error.description}), error.code


@app.errorhandler(Exception)
def handle_unexpected_error(error):
	app.logger.exception("Error inesperado: %s", error)
	return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
	app.run(debug=True, port=5000, host="0.0.0.0")