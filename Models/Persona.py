class Persona:

    def __init__(self, PER_ID, PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO,PER_DOCUMENTO):
        self.__PER_ID           = PER_ID
        self.__PER_UUID         = PER_UUID
        self.__PER_PRI_NOMBRE   = PER_PRI_NOMBRE
        self.__PER_SEG_NOMBRE   = PER_SEG_NOMBRE
        self.__PER_PRI_APELLIDO = PER_PRI_APELLIDO
        self.__PER_SEG_APELLIDO = PER_SEG_APELLIDO
        self.__PER_DOCUMENTO    = PER_DOCUMENTO

    def to_dict(self):
        return {
            "PER_ID": self.__PER_ID,
            "PER_UUID": self.__PER_UUID,
            "PER_PRI_NOMBRE": self.__PER_PRI_NOMBRE,
            "PER_SEG_NOMBRE": self.__PER_SEG_NOMBRE,
            "PER_PRI_APELLIDO": self.__PER_PRI_APELLIDO,
            "PER_SEG_APELLIDO": self.__PER_SEG_APELLIDO,
            "PER_DOCUMENTO": self.__PER_DOCUMENTO
        }