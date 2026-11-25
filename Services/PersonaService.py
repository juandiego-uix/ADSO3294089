from flask import current_app
from Models.Persona import Persona
import uuid


class PersonaRelacionadaError(Exception):
    pass


class personaService:
    @staticmethod
    def add(data):
        persona_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_PERSONA
                 (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO,
                  PER_SEG_APELLIDO, PER_DOCUMENTO)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            c.execute(sql, (persona_uuid, data["pri_nombre"], data["seg_nombre"],
                            data["pri_apellido"], data["seg_apellido"],
                            data["documento"]))
            c.connection.commit()
            return Persona(c.lastrowid, persona_uuid, data["pri_nombre"],
                           data["seg_nombre"], data["pri_apellido"],
                           data["seg_apellido"], data["documento"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_PERSONA")
            return [Persona(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(per_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_PERSONA SET PER_PRI_NOMBRE = %s,
                 PER_SEG_NOMBRE = %s, PER_PRI_APELLIDO = %s,
                 PER_SEG_APELLIDO = %s, PER_DOCUMENTO = %s
                 WHERE PER_UUID = %s"""
        try:
            c.execute(sql, (data["pri_nombre"], data["seg_nombre"],
                            data["pri_apellido"], data["seg_apellido"],
                            data["documento"], per_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(per_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute(
                """SELECT
                       (SELECT COUNT(*) FROM T_APRENDIZ
                        WHERE APR_PER_ID = persona.PER_ID),
                       (SELECT COUNT(*) FROM T_INSTRUCTOR
                        WHERE INS_PER_ID = persona.PER_ID),
                       (SELECT COUNT(*) FROM T_MATRICULA
                        WHERE MAT_PER_ID = persona.PER_ID)
                   FROM T_PERSONA AS persona
                   WHERE persona.PER_UUID = %s""",
                (per_uuid,)
            )
            dependencies = c.fetchone()
            if dependencies is None:
                return False

            labels = ("aprendices", "instructores", "matrículas")
            related = [
                f"{count} {label}"
                for count, label in zip(dependencies, labels)
                if count
            ]
            if related:
                raise PersonaRelacionadaError(
                    "No se puede eliminar la persona porque tiene registros "
                    f"relacionados: {', '.join(related)}."
                )

            c.execute("DELETE FROM T_PERSONA WHERE PER_UUID = %s", (per_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        except PersonaRelacionadaError:
            c.connection.rollback()
            raise
        except Exception as error:
            c.connection.rollback()
            error_code = error.args[0] if error.args else None
            if error_code == 1451:
                raise PersonaRelacionadaError(
                    "No se puede eliminar la persona porque tiene otros "
                    "registros relacionados."
                ) from error
            raise
        finally:
            c.close()
