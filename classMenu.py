import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.op1,
                            2: self.op2,
                            3: self.op3,
                            4: self.op4,
                            0: self.salir
                        }
    def opcion(self,op, ConAl, ConMat):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4:
            func(ConAl, ConMat)
        else:
            func()
    def mostarMenu(self):
        print("1: Cargar datos\n2: Mostrar promedio de un alumno\n3: Informar los estudiantes que aprobaron en forma promocional\n4: Obtener listado de alumnos\n0: Salir del programa")
    def op1(self, ConAl, ConMat):
        os.system("cls")
        ConAl.carga()
        print(ConAl)
        ConMat.carga()
    def op2(self, ConMat):
        os.system("cls")
        print("Promedios\n")
        dni=int(input ("ingrese dni del alumno a buscar: "))
        r=ConMat.promedioSinAplazo(dni)
        print(f"dni: {dni}")
        print("Promedio sin aplazos: {:.2f}".format(r))
        r=ConMat.promedioConAplazo(dni)
        print ("Promedio con aplazos: {:.2f}".format(r))
    def op3(self, ConAl, ConMat):
        os.system("cls")
        nom = str(input("ingrese nombre de materia: "))
        ConMat.promocionales(nom, ConAl)
    def opc4(self, ConAl, ConMat):
        print("Alumnos\n")
        os.system("cls")
        ConAl.ordenar()
        print(ConAl)
    def salir(self):
        pass