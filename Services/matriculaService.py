from flask import current_app
from Models.matricula import matricula
import uuid

class matriculaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
            uuid_mat = uuid.uuid4()
            c = current_app.mysql.connection.cursor()
            sql = """ INSERT INTO T_MATRICULA ( MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION)
                 VALUES (%S, %S, %S) """
            c.execute(sql, (uuid_mat, data["estado"], data["fecha_inscripcion"]))
            c.connection.commit()
            id = c.lastrowid
            c.close()
            respuesta = {"id,":id,"MAT_UUID": uuid_mat,
                         "estado":data["estado"],
                         "fecha_inscripcion":data["fecha_inscripcion"]}
            return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_matricula"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""
