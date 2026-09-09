from flask import current_app
from Models.Instructor import Instructor
import uuid

class instructorService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_instructor = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD,
             INS_PER_ID) VALUES (%s, %s, %s) """
        c.execute(sql, (uuid_instructor, data["especialidad"], data["per_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id":id,"INS_UUID": uuid_instructor,
                     "especialidad":data["especialidad"], "per_id":data["per_id"]}
        return respuesta

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_Instructor"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        c.close()
        return data or []
