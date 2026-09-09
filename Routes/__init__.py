from .aprendiz_bp import apr_bp
from .persona_bp import persona_bp
from .curso_bp import curso_bp
from .instructor_bp import instructor_bp
from .imparte_bp import imparte_bp
from .matricula_bp import matricula_bp
from .evaluacion_bp import evaluacion_bp
from .materiaEvalua_bp import materia_evalua_bp



def loadRoutes(app):

    app.register_blueprint(apr_bp, url_prefix='/aprendices')
    app.register_blueprint(persona_bp, url_prefix='/personas')
    app.register_blueprint(curso_bp, url_prefix='/cursos')
    app.register_blueprint(instructor_bp, url_prefix='/instructores')
    app.register_blueprint(imparte_bp, url_prefix='/imparte')
    app.register_blueprint(matricula_bp, url_prefix='/matriculas')
    app.register_blueprint(evaluacion_bp, url_prefix='/evaluaciones')
    app.register_blueprint(materia_evalua_bp, url_prefix='/materia-evalua')

