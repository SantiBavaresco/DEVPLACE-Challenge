#Challenge Algoritmos
#EJ 4

import random
player1, player2 = "", ""

def ia():
    """
        Esta funcion toma una decion aleatoria para poder jugar contra el Jugador 1
        return:
            devuelve el value de la key seleccionada aleatoriamente
    """
    posibilidades = {1:"p", 2:"a", 3:"t"}
    aleatorio = random.randrange(1,4)
    return posibilidades[aleatorio]

def comparacion(player1,player2):
    """
        Esta funcion compara las jugadas del player1 y el player2 y determina quien gano imprimiendolo por pantalla
        arg:
            player1 : string de la jugada del jugador 1
            player2 : string de la jugada del jugador 2
    """
    if ((player1 == "p") and (player2 == "p")) or ((player1 == "a") and (player2 == "a")) or ((player1 == "t") and (player2 == "t")):
        print("Es un empate")
    elif ((player1 == "p") and (player1 == "a")) or ((player1 == "a") and (player2 == "t")) or ((player1 == "t") and (player2 == "p")):
        print("Gano el Jugador 2")
    elif ((player1 == "p") and (player2 == "t")) or ((player1 == "t") and (player2 == "a")) or ((player1 == "a") and (player2 == "p")):
        print("Gano el Jugador 1")

def pvp(player1,player2):
   """
        Esta funcion determina el modo de juego player vs player(jugador contra jugador), donde toma la jugada de cada player y 
        luego las compara para saber quien gano.
        En caso de que alguno de los jugadores ingrese como jugada la "m" el juego terminara
        arg:
            player1 : string de la jugada del jugador 1 vacio por defecto ("")
            player2 : string de la jugada del jugador 2 vacio por defecto ("")
   """
    while (player1 != "m" ) or (player2 != "m"):
        player1 = input("Turno Jugador 1: ")
        if player1 == "m": break
        player2 = input("Turno Jugador 2: ")
        if player2 == "m": break
        comparacion(player1,player2)
        print("\n")

def pve(player1):
    """
        Esta funcion determina el modo de juego player vs enviriomente(jugador contra ambiente), donde toma la jugada del player1 y 
        ia genera su propia jugadam luego las compara para saber quien gano.
        En caso de que el player1 ingrese como jugada la "m" el juego terminara
        arg:
            player1 : string de la jugada del jugador 1 vacio por defecto ("")
            player2 : string de la jugada del jugador 2 vacio por defecto ("")
   """
    while (player1 != "m" ):
        player1 = input("\nTurno Jugador 1: ")
        if player1 == "m": break
        player2 = ia() 
        print("Turno Jugador 2: {}\n".format(player2))
        comparacion(player1,player2)
    print("\n")



#Menu basico
print("Reglas Piedra-Papel-Tijera")
print("Controles:\n    ‘P’ representa piedra.\n    ‘A’ representa papel. \n    ‘T’ representa tijera)\n\n    ‘M’ Para Salir del Juego.\n")
print("Modo de juego:\n    1- PVP\n    2- PVE")

#Seleccion del modo de juego
modo_juego = input()
if (modo_juego == "1"):
    pvp(player1,player2)
elif (modo_juego == "2"):
    pve(player1)
