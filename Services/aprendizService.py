from flask import current_app
from Models.Aprendiz import Aprendiz
import uuid

class aprendizService:
    @staticmethod
    def add(data):
        uuid_apr = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
               VALUES (%s, %s, %s) """
        try:
            c.execute(sql, (uuid_apr, data["fecha_nac"], data["per_id"]))
            c.connection.commit()
            return Aprendiz(
                c.lastrowid,
                uuid_apr,
                data["fecha_nac"],
                data["per_id"]
            ).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_APRENDIZ")
            return [Aprendiz(*fila).to_dict() for fila in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def delete(apr_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_APRENDIZ WHERE APR_UUID = %s", (apr_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def update(apr_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_APRENDIZ
                 SET APR_FECHA_NAC = %s, APR_PER_ID = %s
                 WHERE APR_UUID = %s"""
        try:
            c.execute(sql, (data["fecha_nac"], data["per_id"], apr_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()