from flask import current_app
from Models.evaluacion import evaluacion
import uuid


class evaluacionService:
    @staticmethod
    def add(data):
        evaluacion_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_EVALUACION
                 (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA)
                 VALUES (%s, %s, %s, %s, %s)"""
        try:
            c.execute(sql, (evaluacion_uuid, data["nombre"], data["codigo"],
                            data["porcentaje"], data["fecha"]))
            c.connection.commit()
            return evaluacion(c.lastrowid, evaluacion_uuid, data["nombre"],
                              data["codigo"], data["porcentaje"],
                              data["fecha"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_EVALUACION")
            return [evaluacion(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(eva_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_EVALUACION SET EVA_NOMBRE = %s,
                 EVA_CODIGO = %s, EVA_PORCENTAJE = %s, EVA_FECHA = %s
                 WHERE EVA_UUID = %s"""
        try:
            c.execute(sql, (data["nombre"], data["codigo"], data["porcentaje"],
                            data["fecha"], eva_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(eva_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_EVALUACION WHERE EVA_UUID = %s", (eva_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
