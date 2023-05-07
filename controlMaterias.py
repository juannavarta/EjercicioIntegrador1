from classAprobadas import MateriasAprobadas
from controlAlumnos import ControlAlumnos
import csv

class ControlMaterias:
    __mat = []

    def __init__(self):
        __mat = []
    def __str__(self):
        st = ""
        for i in range (len(self.__mat)):
            s += str(self.__mat[i].getDNI()) + "," + str(self.__mat[i].getNom()) + "," + str(self.__mat[i].getFecha()) + "," + str(self.__mat[i].getNota()) + "," + str(self.__mat[i].getAp()) + "\n"
        return st
    def getLista(self):
        return self.__mat
    def carga(self):
        archivo = open("C://Users//csv//materiasAprobadas.csv", "r")
        reader = csv.reader (archivo, delimiter=";")
        flag = True
        for fila in reader:
            if flag:
                flag = False
            else:
                dni = int (fila[0])
                nombre = fila[1]
                fecha = fila[2]
                nota = int (fila[3])
                aprob = fila [4]
                Materia = MateriasAprobadas(dni, nombre, fecha, nota, aprob)
                self.__mat.append(Materia)
        print ("carga de materias aprobadas lista")
        archivo.close()
    def buscarDni(self, dni):
        indice=0
        val = None
        flag=False
        while not flag and indice < len(self.__mat):
            if self.__mat[indice].getDNI() == dni:
                flag=True
                val=indice
            else: indice+=1
        if val==None:
            print("Error, Alumno no encontrado")
        return val
    def promedioConAplazo(self, dni):
        c = 0
        suma = 0
        for i in range(len(self.__mat)):
            if self.__mat[i].getDNI() == dni:
                suma += self.__mat[i].getNota()
                c+=1
        prom = suma/c
        return prom
    def promedioSinAplazo(self, dni):
        c = 0
        suma = 0
        for i in range(len(self.__mat)):
            if self.__mat[i].getDNI() == dni and self.__mat[i].getNota()>=4:
                suma += self.__mat[i].getNota()
                c=c+1
        prom = suma/c
        return prom
    def promocionales(self, nom, ConAl):
        print("|{:^10} {:^10} {:^10} {:^10} {:^10}|".format("DNI", "Nombre y Apellido", "Fecha", "Nota", "Año que cursa\n"))
        for materia in self.__mat:
            if nom == materia.getNom() and materia.getAp()=="P":
                d = materia.getDNI()
                i = ConAl.buscarDni(d)
                alumno = ConAl.getAlumno(i)
                nya = alumno.getNom() + alumno.getApellido()
                print ("|{:^10} {:^10} {:^10} {:^10} {:^10}|". format(alumno.getDNI(), nya, materia.getFecha(), materia.getNota(), alumno.getAño()))