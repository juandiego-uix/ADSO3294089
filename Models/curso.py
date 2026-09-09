class curso:

    def __init__(self, CUR_ID, CUR_UUID, CUR_NOMBRE, CUR_CODIGO,CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION):
        self.__CUR_ID           = CUR_ID
        self.__CUR_UUID         = CUR_UUID
        self.__CUR_NOMBRE       = CUR_NOMBRE
        self.__CUR_CODIGO       = CUR_CODIGO
        self.__CUR_DURACION     = CUR_DURACION
        self.__CUR_COSTO        = CUR_COSTO
        self.__CUR_DESCRIPCION  = CUR_DESCRIPCION


    def to_dict(self):
        return {
            "CUR_ID": self.__CUR_ID,
            "CUR_UUID": self.__CUR_UUID,
            "CUR_NOMBRE": self.__CUR_NOMBRE,
            "CUR_CODIGO": self.__CUR_CODIGO,
            "CUR_DURACION": self.__CUR_DURACION,
            "CUR_COSTO": self.__CUR_COSTO,
            "CUR_DESCRIPCION": self.__CUR_DESCRIPCION
        }