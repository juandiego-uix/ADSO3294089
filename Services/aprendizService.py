from flask import current_app
from Models.Aprendiz import Aprendiz
import uuid


class aprendizService:

    @staticmethod
    def add(data):
        uuid_apr = str(uuid.uuid4())

        c = current_app.mysql.connection.cursor()

        sql = """INSERT INTO T_APRENDIZ 
                 (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
                 VALUES (%s, %s, %s)"""
        try:
            c.execute(
                sql,
                (
                    uuid_apr,
                    data["fecha_nac"],
                    data["per_id"]
                )
            )

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
        sql = """SELECT aprendiz.APR_ID,
                        aprendiz.APR_UUID,
                        aprendiz.APR_FECHA_NAC,
                        persona.PER_PRI_NOMBRE,
                        persona.PER_SEG_NOMBRE,
                        persona.PER_PRI_APELLIDO,
                        persona.PER_SEG_APELLIDO,
                        persona.PER_DOCUMENTO
                 FROM T_APRENDIZ AS aprendiz
                 INNER JOIN T_PERSONA AS persona
                 ON persona.PER_ID = aprendiz.APR_PER_ID"""

        c = current_app.mysql.connection.cursor()

        try:
            c.execute(sql)
            data = c.fetchall()

            data = [
                Aprendiz(
                    x[0],
                    x[1],
                    x[2],
                    {
                        "nombres": " ".join(
                            str(value).strip()
                            for value in (x[3], x[4])
                            if value is not None and str(value).strip()
                        ),
                        "apellidos": " ".join(
                            str(value).strip()
                            for value in (x[5], x[6])
                            if value is not None and str(value).strip()
                        ),
                        "cedula": x[7]
                    }
                ).to_dict()
                for x in data
            ]

            return data

        finally:
            c.close()

    @staticmethod
    def delete(apr_uuid):
        c = current_app.mysql.connection.cursor()

        try:
            c.execute(
                "DELETE FROM T_APRENDIZ WHERE APR_UUID = %s",
                (apr_uuid,)
            )

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
            c.execute(
                sql,
                (
                    data["fecha_nac"],
                    data["per_id"],
                    apr_uuid
                )
            )

            c.connection.commit()

            return c.rowcount > 0

        finally:
            c.close()
