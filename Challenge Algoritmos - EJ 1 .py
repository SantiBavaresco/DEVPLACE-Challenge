#Challenge Algoritmos
#EJ 1

a = int(input("Ingrese el primer valor del intevalo: "))
b = int(input("Ingrese el segundo valor del intevalo: "))

for i in range(a,b+1):
    print("El valor {}{} es un numero primo.".format(i, "" if (i % 2 == 0) else " no")) 
