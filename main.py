import os
from classMenu import Menu
from controlAlumnos import ControlAlumnos
from controlMaterias import ControlMaterias

if __name__ == "__main__":
    manejador = ""
    flag = False
    menu = Menu()
    os.system('cls')
    while not flag:
        menu.mostarMenu()
        opcion = int (input("Ingrese una opcion: "))
        conAl = ControlAlumnos(3,5)
        conMat = ControlMaterias()
        menu.opcion(opcion, conAl, conMat)
        if opcion==0:
            flag = True
        os.system('pause')
        os.system('cls')
    os.system('exit')