from flask import current_app
from Models.curso import curso
import uuid


class cursoService:
    @staticmethod
    def add(data):
        curso_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_CURSO
                 (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION,
                  CUR_COSTO, CUR_DESCRIPCION)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            c.execute(sql, (curso_uuid, data["nombre"], data["codigo"],
                            data["duracion"], data["costo"],
                            data["descripcion"]))
            c.connection.commit()
            return curso(c.lastrowid, curso_uuid, data["nombre"], data["codigo"],
                         data["duracion"], data["costo"],
                         data["descripcion"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_CURSO")
            return [curso(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(cur_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_CURSO SET CUR_NOMBRE = %s, CUR_CODIGO = %s,
                 CUR_DURACION = %s, CUR_COSTO = %s, CUR_DESCRIPCION = %s
                 WHERE CUR_UUID = %s"""
        try:
            c.execute(sql, (data["nombre"], data["codigo"], data["duracion"],
                            data["costo"], data["descripcion"], cur_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(cur_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_CURSO WHERE CUR_UUID = %s", (cur_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
