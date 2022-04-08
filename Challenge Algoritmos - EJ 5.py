#Challenge Algoritmos
#EJ 5

def resultado(salario,porcentaje):
    """
        Esta funcion calcua e imprime por pantalla el salario total con % de aumento en funcion de los parametros de entrada
        arg:
            salario: float correspondiente al salario de la persona
            porcentaje: int correpondiente al procentaje segun la edad
    """
    salario_real = salario + ( (salario / 100) * porcentaje )
    print("El salario es de ${} mas un {}%, sumando un total de ${}"
            .format(salario, porcentaje, salario_real))
    
def comparacion_por_edad(persona):
    """
        Esta funcion determina la division por edades y sus porcentaje de aumento para cada edad
        arg:
            persona : diccionario de entrada con los datos de la persona (nombre, edad, salario)
    """
    #lista con los valores de aumento en porcentaje del salario
    porcentaje_de_aumento = [0, 5, 10, 15]

    if (persona["Edad"] < 16):
        print("No tiene edad para trabajar")

    elif ((persona["Edad"] > 19) and (persona["Edad"] < 50)):
        resultado(persona["Salario"],porcentaje_de_aumento[1])
        
    elif ((persona["Edad"] > 51) and (persona["Edad"] < 60)):
        resultado(persona["Salario"],porcentaje_de_aumento[2])

    elif (persona["Edad"] > 60) :
        resultado(persona["Salario"],porcentaje_de_aumento[3])

    else:      #las personas con 17, 18 y 19 años reciben 0% de aumento
        resultado(persona["Salario"],porcentaje_de_aumento[0])

#Carga de datos de 1 persona en un diccionario.
persona = {"Nombre" : "", "Edad" : 0, "Salario" : 0.0}

persona["Nombre"] = input("Ingrese el nombre de la persona: ")
persona["Edad"] = int(input("Ingrese la edad de la persona: "))
persona["Salario"] = float(input("Ingrese el salario de la persona: "))

comparacion_por_edad(persona)