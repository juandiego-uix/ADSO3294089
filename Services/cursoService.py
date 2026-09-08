from flask import current_app
from Models.curso import curso
import uuid 

class cursoService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_cur = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_CURSO ( CUR_UUID, CUR_NOMBRE, CUR_CODIGO)
             VALUES (%S, %S, %S) """
        c.execute(sql, (uuid_cur, data["nombre"], data["codigo"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id,":id,"CUR_UUID": uuid_cur,
                     "nombre":data["nombre"],
                     "codigo":data["codigo"]}
        return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_CURSO"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""
