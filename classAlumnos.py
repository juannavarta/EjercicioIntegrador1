class Alumnos:
    __dni = 0
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __anio = 0

    def __init__(self, dni=0, apellido="", nombre="", carrera="", anio=0):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio = anio
    def getDNI(self):
        return self.__dni
    def getNom(self):
        return self.__nombre
    def getApe(self):
        return self.__apellido
    def getCar(self):
        return self.__carrera
    def getAnio(self):
        return self.__anio
    def __gt__(self, otro):
        a = str(self.__anio) + self.__nombre() + self.__apellido
        b = str(otro.getAño) + otro.getNom + otro.getApe
        return (a>b)