from flask import current_app
from Models.Aprendiz import Aprendiz
import uuid 

class aprendizService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_apr = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
               VALUES (%s, %s, %s) """
        c.execute(sql, (uuid_apr, data["fecha_nac"],
                        data["per_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"APR_UUID": uuid_apr,
                     "fecha_nac":data["fecha_nac"],
                     "per_id":data ["per_id"]}
        return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        c.close()
        return data
