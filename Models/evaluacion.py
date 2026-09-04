class evaluacion:
    def __init__(self, EVA_ID, EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA):
        self.__EVA_ID            = EVA_ID
        self.__EVA_UUID          = EVA_UUID
        self.__EVA_NOMBRE        = EVA_NOMBRE
        self.__EVA_CODIGO        = EVA_CODIGO
        self.__EVA_PORCENTAJE    = EVA_PORCENTAJE
        self.__EVA_FECHA         = EVA_FECHA

    def to_dict(self):
        return {
            "EVA_ID": self.__EVA_ID,
            "EVA_UUID": self.__EVA_UUID,
            "EVA_NOMBRE": self.__EVA_NOMBRE,
            "EVA_CODIGO": self.__EVA_CODIGO,
            "EVA_PORCENTAJE": self.__EVA_PORCENTAJE,
            "EVA_FECHA": self.__EVA_FECHA
        }