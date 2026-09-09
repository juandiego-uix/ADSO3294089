from flask import current_app
from Models.matricula import matricula
import uuid

class matriculaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_mat = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_MATRICULA (MAT_UUID, MAT_ESTADO,
             MAT_FECHA_INCRIPCION, MAT_APR_ID, MAT_CUR_ID)
             VALUES (%s, %s, %s, %s, %s) """
        c.execute(sql, (uuid_mat, data["estado"], data["fecha_inscripcion"],
                        data["apr_id"], data["cur_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"MAT_UUID": uuid_mat,
                     "estado":data["estado"], "fecha_inscripcion":data["fecha_inscripcion"],
                     "apr_id":data["apr_id"], "cur_id":data["cur_id"]}
        return respuesta

    def delete():
        c = current_app.mysql.connection.cursor()
        sql = """DELETE FROM T_MATRICULA WHERE MAT_UUID = %s """
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
        sql = "SELECT * FROM T_matricula"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        c.close()
        return data or []
