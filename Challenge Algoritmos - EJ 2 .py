#Challenge Algoritmos
#EJ 2

lista = []
suma = 0
for i in range(1,6):
    print("Ingrese el valor numero {}".format(i))
    lista.append(int(input(""))) 
    suma = lista[i-1] + suma
lista.reverse()

print("La suma de todos los valores es = {}".format(suma))
print("La lista de numeros a la inversa es : ", lista)
