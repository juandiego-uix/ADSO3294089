from flask import current_app
from Models.Instructor import Instructor
import uuid


class instructorService:
    @staticmethod
    def add(data):
        instructor_uuid = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_INSTRUCTOR
                 (INS_UUID, INS_ESPECIALIDAD, INS_PER_ID)
                 VALUES (%s, %s, %s)"""
        try:
            c.execute(sql, (instructor_uuid, data["especialidad"], data["per_id"]))
            c.connection.commit()
            return Instructor(c.lastrowid, instructor_uuid, data["especialidad"],
                              data["per_id"]).to_dict()
        finally:
            c.close()

    @staticmethod
    def show():
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("SELECT * FROM T_INSTRUCTOR")
            return [Instructor(*row).to_dict() for row in c.fetchall()]
        finally:
            c.close()

    @staticmethod
    def update(ins_uuid, data):
        c = current_app.mysql.connection.cursor()
        sql = """UPDATE T_INSTRUCTOR SET INS_ESPECIALIDAD = %s,
                 INS_PER_ID = %s WHERE INS_UUID = %s"""
        try:
            c.execute(sql, (data["especialidad"], data["per_id"], ins_uuid))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()

    @staticmethod
    def delete(ins_uuid):
        c = current_app.mysql.connection.cursor()
        try:
            c.execute("DELETE FROM T_INSTRUCTOR WHERE INS_UUID = %s", (ins_uuid,))
            c.connection.commit()
            return c.rowcount > 0
        finally:
            c.close()
