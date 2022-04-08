#Challenge Algoritmos
#EJ 3

lista = [10, 30, 45, 25, 15]

def menor_a_mayor_1(lista_original):
    """
        Esta funcion ordena de menor a mayor una lista de elementos
        arg:
            lista_original : lista con los elementos desordenados
    """
    for i in range(4):
        if lista_original[i] > lista_original[i+1]:
            aux = lista_original[i]
            lista_original[i] = lista_original[i+1]
            lista_original[i+1] = aux
    return lista_original

def menor_a_mayor_2(lista_original):
    """
        Esta funcion ordena de menor a mayor una lista de elementos con el metodo sort()
        arg:
            lista_original : lista con los elementos desordenados
    """
    lista_original.sort()
    return lista_original

def menor_a_mayor_3(lista_original):
    """
        Esta funcion ordena de menor a mayor una lista de elementos con la funcion sorted(), como output, 
        devuelve una permutación del objeto iterable ordenado según la función indicada (al no indicar ninguna funcion lo ordena de
        manera descendente)
        arg:
            lista_original : lista con los elementos desordenados
    """
    return sorted(lista_original,  reverse = True)
    
print(menor_a_mayor_1(lista))