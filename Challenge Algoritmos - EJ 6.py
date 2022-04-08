#Challenge Algoritmos
#EJ 6

from numpy import random

i = True
#repeticion infinta hasta que se cumpla la condicion de salida
while i != False:
    #generacion de numeros aletorios en un array
    numeros_aleatorios = random.randint(0, 1001, size = 3)
    #comparacion de las tres posiones del array para cumplir con la condicion de "par, par, impar"
    if (numeros_aleatorios[0] % 2 == 0) and (numeros_aleatorios[1] % 2 == 0) and (numeros_aleatorios[2] % 2 != 0):
        print("Se consiguió par, par, impar")
        print(numeros_aleatorios)
        break

    print("No se consiguió par, par, impar")
    print(numeros_aleatorios, end="\n")
    
    input()


#EJ 6 de manera recursiva

from numpy import random

def aleatorios():  
    """
        Esta funcion genera numeros aleatorios de manera recursiva hasta conseguir la condicion de salida de la recursividad.
    """ 
    numeros_aleatorios = random.randint(0, 1001, size = 3)
    if (numeros_aleatorios[0] % 2 == 0) and (numeros_aleatorios[1] % 2 == 0) and (numeros_aleatorios[2] % 2 != 0):
        print("Se consiguió par, par, impar")
        print(numeros_aleatorios)
        return True
    print("No se consiguió par, par, impar")
    print(numeros_aleatorios, end="\n")
    aleatorios()

aleatorios()
