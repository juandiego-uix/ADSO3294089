from flask import current_app
from Models.matricula import matricula
import uuid


class matriculaService:
    @staticmethod
    def add(data):
        matricula_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_MATRICULA
                 (MAT_UUID, MAT_FECHA, MAT_ESTADO, MAT_PER_ID, MAT_CUR_ID)
                 VALUES (%s, %s, %s, %s, %s)"""
        try:
            c.execute(sql, (matricula_uuid, data["fecha"], data["estado"],
                            data["per_id"], data["cur_id"]))
            c.connection.commit()
            return matricula(c.lastrowid, matricula_uuid, data["fecha"],
                             data["estado"], data["per_id"],
                             data["cur_id"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_MATRICULA")
            return [matricula(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(mat_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_MATRICULA SET MAT_FECHA = %s,
                 MAT_ESTADO = %s, MAT_PER_ID = %s, MAT_CUR_ID = %s
                 WHERE MAT_UUID = %s"""
        try:
            c.execute(sql, (data["fecha"], data["estado"], data["per_id"],
                            data["cur_id"], mat_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(mat_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_MATRICULA WHERE MAT_UUID = %s", (mat_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
