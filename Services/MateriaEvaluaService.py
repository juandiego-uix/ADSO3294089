from flask import current_app
from Models.materia_evalua import materia_evalua
import uuid

class materia_evaluaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_mat_eva = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA,
             MATE_EVA_ID, MATE_MAT_ID) VALUES (%s, %s, %s, %s) """
        c.execute(sql, (uuid_mat_eva, data["nota"], data["eva_id"],
                        data["mat_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"MATE_UUID": uuid_mat_eva,
                     "nota":data["nota"], "eva_id":data["eva_id"],
                     "mat_id":data["mat_id"]}
        return respuesta

    def delete():
        c = current_app.mysql.connection.cursor()
        sql = """DELETE FROM T_MAT_EVA WHERE MATE_UUID = %s """
        c.execute(sql, [uuid])
        c.connection.commit()
        if  c.lastrowid >0:
            codigo = 200
        else:
                codigo = 400
        c.close()
        return codigo

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_materia_evalua"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        c.close()
        return data or []
