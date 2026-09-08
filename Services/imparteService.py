from flask import current_app
from Models.imparte import imparte
import uuid

class imparteService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
            uuid_imp = uuid.uuid4()
            c = current_app.mysql.connection.cursor()
            sql = """ INSERT INTO T_IMPARTE ( IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION)
                 VALUES (%S, %S, %S) """
            c.execute(sql, (uuid_imp, data["rol"], data["fecha_asignacion"]))
            c.connection.commit()
            id = c.lastrowid
            c.close()
            respuesta = {"id,":id,"IMP_UUID": uuid_imp,
                         "rol":data["rol"],
                         "fecha_asignacion":data["fecha_asignacion"]}
            return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_imparte"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        # c.close()
        return ""
