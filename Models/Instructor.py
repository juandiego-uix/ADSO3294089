class Instructor:

    def __init__(self, INS_ID, INS_UUID, INS_ESPECIALIDAD, INS_PER_ID):
        self.__INS_ID           = INS_ID
        self.__INS_UUID         = INS_UUID
        self.__INS_ESPECIALIDAD = INS_ESPECIALIDAD
        self.__INS_PER_ID       = INS_PER_ID


    def to_dict(self):
        return {
            "INS_ID": self.__INS_ID,
            "INS_UUID": self.__INS_UUID,
            "INS_ESPECIALIDAD": self.__INS_ESPECIALIDAD,
            "INS_PER_ID": self.__INS_PER_ID
        }