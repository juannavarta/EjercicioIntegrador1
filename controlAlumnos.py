import numpy as np
from classAlumnos import Alumnos
import csv

class ControlAlumnos:
    __cant = 0
    __dim = 0
    __incr = 5

    def __init__(self, xDim, incr=5):
        self.__alum = np.empty(xDim, dtype=Alumnos)
        self.__cant = 0
        self.__dim = xDim
    def getAlum(self, i):
        return self.__alum[i]
    def agregaAlum(self, n):
        if self.__cant==self.__dim:
            self.__dim=self.__dim+self.__incr
            self.__alum.resize(self.__dim, refcheck=False)
        self.__alum[self.__cant]=n
        self.__cant=self.__cant+1
    def __str__(self):
        st = ""
        for i in range(len(self.__alum)):
            st = st + str(self.__alum[i].getDNI()) + ',' + str(self.__alum[i].getApe()) + ',' + str(self.__alum[i].getNom) + ',' + str(self.__alum[i].getAnio())
        return st
    def carga(self):
        archivo = open("C://Users//csv//alumnos.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        flag = True
        for fila in reader:
            if flag==True:
                flag = False
            else:
                dni=int(fila[0])
                ape=fila[1]
                nom=fila[2]
                carrera=fila[3]
                anio=fila[4]
                alumno = Alumnos(dni, ape, nom, carrera, anio)
                self.agregaAlum(alumno)
        archivo.close()
    def ordenar(self):
        flag = True
        while flag:
            flag = False
            for i in range(len(self.__alum)-1):
                if self.__alum[i] > self.__alum[i+1]:
                    self.__alum[i],self.__alum[i+1]=self.__alum[i+1],self.__alum[i]
                    flag = True
    def buscaDNI(self, dni):
        val = None
        flag = False
        i = 0
        while i < self.__cantidad and not flag:
            if dni == self.__alum[i].getDNI():
                val = i
                flag = True
            else:
                i += 1
        if val != None:
            print(self.__alum[val]) 
        else:
            print(f"No existe ningún alumno con DNI {dni}")
        return val
