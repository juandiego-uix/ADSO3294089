class Aprendiz:

    def __init__(self, APR_ID, APR_UUID, APR_FECHA_NAC, APR_PER_ID):
        self.__APR_ID       = APR_ID
        self.__APR_UUID     = APR_UUID
        self.__APR_FECHA_NAC= APR_FECHA_NAC
        self.__APR_PER_ID   = APR_PER_ID

    # la tupla se convierte en un obj y ese obj en dic
    def to_dict(self):
        return {
            "APR_ID": self.__APR_ID,
            "APR_UUID": self.__APR_UUID,
            "APR_FECHA_NAC": self.__APR_FECHA_NAC,
            "APR_PER_ID": self.__APR_PER_ID
        }
