from flask import current_app
from Models.Persona import Persona
import uuid

class PersonaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
        uuid_persona = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_PERSONA ( PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOC)
             VALUES (%s, %s, %s, %s, %s, %s) """
        c.execute(sql, (uuid_persona, data["primer_nombre"], data["segundo_nombre"], data["primer_apellido"], data["segundo_apellido"], data["documento"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id": id, "PER_UUID": uuid_persona,
                     "primer_nombre": data["primer_nombre"],
                     "segundo_nombre": data["segundo_nombre"],
                     "primer_apellido": data["primer_apellido"],
                     "segundo_apellido": data["segundo_apellido"],
                     "documento": data["documento"]}
        return respuesta

    @staticmethod
    def delete():
        c = current_app.mysql.connection.cursor()
        sql = """DELETE FROM T_PERSONA WHERE PER_UUID = %s """
        c.execute(sql, [uuid])
        c.connection.commit()
        if  c.lastrowid >0:
            codigo = 200
        else:
                codigo = 400
        c.close()
        return codigo

    @staticmethod
    def update():
        pass

    @staticmethod
    def show():
        sql = "SELECT * FROM T_Persona"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        c.close()
        return data or []
