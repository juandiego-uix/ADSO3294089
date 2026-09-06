from flask import current_app
from Models.Persona import Persona

class PersonaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add():
        pass

    @staticmethod
    def delete():
        pass

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
        # c.close()
        return ""
