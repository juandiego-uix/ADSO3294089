from flask import current_app
from Models.imparte import imparte
import uuid


class imparteService:
    @staticmethod
    def add(data):
        imparte_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_IMPARTE
                 (IMP_UUID, IMP_ROL, IMP_FECHA, IMP_FECHA_ASIGNACION,
                  IMP_CUR_ID, IMP_INS_ID)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            c.execute(sql, (imparte_uuid, data["rol"], data["fecha"],
                            data["fecha_asignacion"], data["cur_id"],
                            data["ins_id"]))
            c.connection.commit()
            return imparte(c.lastrowid, imparte_uuid, data["rol"], data["fecha"],
                           data["fecha_asignacion"], data["cur_id"],
                           data["ins_id"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_IMPARTE")
            return [imparte(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(imp_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_IMPARTE SET IMP_ROL = %s, IMP_FECHA = %s,
                 IMP_FECHA_ASIGNACION = %s, IMP_CUR_ID = %s, IMP_INS_ID = %s
                 WHERE IMP_UUID = %s"""
        try:
            c.execute(sql, (data["rol"], data["fecha"],
                            data["fecha_asignacion"], data["cur_id"],
                            data["ins_id"], imp_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(imp_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_IMPARTE WHERE IMP_UUID = %s", (imp_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
