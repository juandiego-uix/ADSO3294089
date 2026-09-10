class matricula:
    def __init__(self, MAT_ID, MAT_UUID, MAT_FECHA, MAT_ESTADO, MAT_PER_ID, MAT_CUR_ID):
        self.__MAT_ID           = MAT_ID
        self.__MAT_UUID         = MAT_UUID
        self.__MAT_FECHA        = MAT_FECHA
        self.__MAT_ESTADO       = MAT_ESTADO
        self.__MAT_PER_ID       = MAT_PER_ID
        self.__MAT_CUR_ID       = MAT_CUR_ID

    def to_dict(self):
        return {
            "MAT_ID": self.__MAT_ID,
            "MAT_UUID": self.__MAT_UUID,
            "MAT_FECHA": self.__MAT_FECHA,
            "MAT_ESTADO": self.__MAT_ESTADO,
            "MAT_PER_ID": self.__MAT_PER_ID,
            "MAT_CUR_ID": self.__MAT_CUR_ID
        }
