import os
os.system("cls")

menu = '''
    MENU
1.- COMPRAR ENTRADAS
2.- MOSTRAR UBICACIONES DISPONIBLES
3.- VER LSTADO DE ASISTENTES
4.- MOSTRAR GANANCIAS TOTALES
5.- SALIR
Digite opcion: '''

fila1 = [1,2,3,4,5,6,7,8,9,10]
fila2 = [11,12,13,'X','X','X',17,18,19,20]
fila3 = [21,22,23,24,25,26,27,28,29,30]
fila4 = [31,32,'X',34,35,36,37,38,39,40]
fila5 = [41,42,43,44,'X',46,47,48,49,50]
fila6 = [51,52,53,54,55,56,57,58,59,60]
fila7 = [61,62,63,64,65,66,67,68,69,70]
fila8 = [71,72,73,74,75,76,77,78,79,80]
fila9 = [81,82,83,84,85,86,87,88,89,90]
fila10 = [91,92,93,94,95,96,97,98,99,100]

def salir():
    print("Saliendo!")
    print("Nombre: Sebastian Monjes - 10/07/2023")

def comprar():
    while True:
        try:
            cantidad = int(input("Cuantas entradas desea comprar: "))
            if cantidad >= 1 and cantidad <= 3:
                break
            else:
                print("La cantidad de entradas debe ser entre 1 y 3")
        except:
            print("Exepcion en cantidad de entradas")
#end while cantidad
    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)
    print(fila5)
    print(fila6)
    print(fila7)
    print(fila8)
    print(fila9)
    print(fila10)
#Se realiza la muestra del escenario
    while True:
        try:
            asiento = int(input("Ingrese el asiento a comprar: "))
            if asiento >= 1 and asiento <= 10:
                for i in range(len(fila1)):
                    if asiento == fila1[i]:
                        print("Asiento disponible")
                        fila1.insert[i]("X")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 11 and asiento <= 20:
                for i in range(len(fila2)):
                    if asiento == fila2[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 21 and asiento <= 30:
                for i in range(len(fila3)):
                    if asiento == fila3[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 31 and asiento <= 40:
                for i in range(len(fila4)):
                    if asiento == fila4[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 41 and asiento <= 50:
                for i in range(len(fila5)):
                    if asiento == fila5[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 51 and asiento <= 60:
                for i in range(len(fila6)):
                    if asiento == fila6[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 61 and asiento <= 70:
                for i in range(len(fila7)):
                    if asiento == fila7[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 71 and asiento <= 80:
                for i in range(len(fila8)):
                    if asiento == fila8[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 81 and asiento <= 90:
                for i in range(len(fila9)):
                    if asiento == fila9[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            elif asiento >= 91 and asiento <= 100:
                for i in range(len(fila10)):
                    if asiento == fila10[i]:
                        print("Asiento disponible")
                        break
                    else:
                        print("No esta disponible")
                break
            else:
                print("No esta disponible")
        except:
            print("Exepcion en asiento")

def mostrar():
    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)
    print(fila5)
    print(fila6)
    print(fila7)
    print(fila8)
    print(fila9)
    print(fila10)

def verlistado():
    print()

def mostrarganancia():
    print()

#MAIN
while True:
    try:
        opc = int(input(menu))
        if opc == 5:
            salir()
            break
        elif opc == 1:
            comprar()
        elif opc == 2:
            mostrar()
        elif opc == 3:
            verlistado()
        elif opc == 4:
            mostrarganancia()
        else:
            print("Opcion invalida")
    except:
        print("Excepcion en menu")
