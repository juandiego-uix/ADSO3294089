from flask import current_app
from Models.materia_evalua import materia_evalua
import uuid

class materia_evaluaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
            uuid_mat_eva = uuid.uuid4()
            c = current_app.mysql.connection.cursor()
            sql = """ INSERT INTO T_MAT_EVA ( MATE_UUID)
                 VALUES (%S) """
            c.execute(sql, (uuid_mat_eva,))
            c.connection.commit()
            id = c.lastrowid
            c.close()
            respuesta = {"id,":id,"MATE_UUID": uuid_mat_eva}
            return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_materia_evalua"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""
