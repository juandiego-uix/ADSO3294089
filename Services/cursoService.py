from flask import current_app
from Models.curso import curso
import uuid 

class cursoService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_cur = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO,
               CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION)
               VALUES (%s, %s, %s, %s, %s, %s) """
        c.execute(sql, (uuid_cur, data["nombre"], data["codigo"],
                        data["duracion"], data["costo"], data["descripcion"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"CUR_UUID": uuid_cur,
                     "nombre":data["nombre"],
                     "codigo":data["codigo"],
                     "duracion":data["duracion"],
                     "costo":data["costo"],
                     "descripcion":data["descripcion"]}
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
        c.close()
        return data or []
