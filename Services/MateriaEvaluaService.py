from flask import current_app
from Models.materia_evalua import materia_evalua
import uuid


class materiaEvaluaService:
    @staticmethod
    def add(data):
        materia_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_MATERIA_EVALUA
                 (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID)
                 VALUES (%s, %s, %s, %s)"""
        try:
            c.execute(sql, (materia_uuid, data["nota"], data["eva_id"],
                            data["mat_id"]))
            c.connection.commit()
            return materia_evalua(c.lastrowid, materia_uuid, data["nota"],
                                  data["eva_id"], data["mat_id"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_MATERIA_EVALUA")
            return [materia_evalua(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(mate_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_MATERIA_EVALUA SET MATE_NOTA = %s,
                 MATE_EVA_ID = %s, MATE_MAT_ID = %s
                 WHERE MATE_UUID = %s"""
        try:
            c.execute(sql, (data["nota"], data["eva_id"], data["mat_id"], mate_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(mate_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_MATERIA_EVALUA WHERE MATE_UUID = %s", (mate_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
