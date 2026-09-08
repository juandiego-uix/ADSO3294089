from flask import current_app
from Models.evaluacion import evaluacion
import uuid

class evaluacionService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
            uuid_eva = uuid.uuid4()
            c = current_app.mysql.connection.cursor()
            sql = """ INSERT INTO T_EVALUACION ( EVA_UUID, EVA_NOMBRE, EVA_CODIGO)
                 VALUES (%S, %S, %S) """
            c.execute(sql, (uuid_eva, data["nombre"], data["codigo"]))
            c.connection.commit()
            id = c.lastrowid
            c.close()
            respuesta = {"id,":id,"EVA_UUID": uuid_eva,
                         "nombre":data["nombre"],
                         "codigo":data["codigo"]}
            return respuesta
    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_evaluacion"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""
