class MateriasAprobadas:
    __dni = 0
    __mat = ""
    __fecha = ""
    __nota = 0
    __ap = ""

    def __init__(self, dni=0, mat="", fecha="", nota=0, ap=""):
        self.__dni = dni
        self.__mat = mat
        self.__fecha = fecha
        self.__nota = nota
        self.__ap = ap
    def getDNI(self):
        return self.__dni
    def getMat(self):
        return self.__mat
    def getFecha(self):
        return self.__fecha
    def getNota(self):
        return self.__nota
    def getAp(self):
        return self.__ap