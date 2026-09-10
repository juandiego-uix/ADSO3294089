class materia_evalua:
    def __init__(self, MATE_ID, MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID):
        self.__MATE_ID           = MATE_ID
        self.__MATE_UUID         = MATE_UUID
        self.__MATE_NOTA         = MATE_NOTA
        self.__MATE_EVA_ID       = MATE_EVA_ID
        self.__MATE_MAT_ID       = MATE_MAT_ID


    def to_dict(self):
        return {
            "MATE_ID": self.__MATE_ID,
            "MATE_UUID": self.__MATE_UUID,
            "MATE_NOTA": self.__MATE_NOTA,
            "MATE_EVA_ID": self.__MATE_EVA_ID,
            "MATE_MAT_ID": self.__MATE_MAT_ID
        }
