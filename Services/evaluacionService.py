from flask import current_app
from Models.evaluacion import evaluacion
import uuid

class evaluacionService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_eva = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_EVALUACION (EVA_UUID, EVA_NOMBRE,
             EVA_CODIGO, EVA_PORCENTAJE, EVA_DATE)
             VALUES (%s, %s, %s, %s, %s) """
        c.execute(sql, (uuid_eva, data["nombre"], data["codigo"],
                        data["porcentaje"], data["fecha"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"EVA_UUID": uuid_eva,
                     "nombre":data["nombre"], "codigo":data["codigo"],
                     "porcentaje":data["porcentaje"], "fecha":data["fecha"]}
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
        c.close()
        return data
