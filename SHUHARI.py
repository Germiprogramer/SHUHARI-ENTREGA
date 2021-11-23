from random import choice, sample

#Baraja

picas = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4, chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8, chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0X1f0ab): 10, chr(0x1f0ad): 10, chr(0x1f0ae): 10}
corazones = {chr(0x1f0b1): 11, chr(0x1f0b2): 2, chr(0x1f0b3): 3, chr(0x1f0b4): 4, chr(0x1f0b5): 5, chr(0x1f0b6): 6, chr(0x1f0b7): 7, chr(0x1f0b8): 8, chr(0x1f0b9): 9, chr(0x1f0ba): 10, chr(0X1f0bb): 10, chr(0x1f0bd): 10, chr(0x1f0be): 10}
rombos = {chr(0x1f0c1): 11, chr(0x1f0c2): 2, chr(0x1f0c3): 3, chr(0x1f0c4): 4, chr(0x1f0c5): 5, chr(0x1f0c6): 6, chr(0x1f0c7): 7, chr(0x1f0c8): 8, chr(0x1f0c9): 9, chr(0x1f0ca): 10, chr(0X1f0cb): 10, chr(0x1f0cd): 10, chr(0x1f0ac): 10}
treboles = {chr(0x1f0d1): 11, chr(0x1f0d2): 2, chr(0x1f0d3): 3, chr(0x1f0d4): 4, chr(0x1f0d5): 5, chr(0x1f0d6): 6, chr(0x1f0d7): 7, chr(0x1f0d8): 8, chr(0x1f0d9): 9, chr(0x1f0da): 10, chr(0X1f0db): 10, chr(0x1f0dd): 10, chr(0x1f0de): 10}

baraja = {**picas, **corazones, **rombos, **treboles}

#Valor de cada carta

print("Cartas {}:".format(" ".join(baraja.keys())))
print("Valores de las cartas {}".format(list(baraja.values())))

for carta, valor in baraja.items():
    print("Las cartas {} valen {}".format(carta, valor))

lista_baraja = list(baraja)

#Mano del jugador

print("Su mano es:", end=" ")
carta_jugador1 = choice(lista_baraja)
score_jugador = baraja[carta_jugador1]
print(carta_jugador1, end=" ")
carta_jugador2 = choice(lista_baraja)
score_jugador += baraja[carta_jugador2]
print(carta_jugador2, end=" ")
print("Su puntuación es de: ", score_jugador)

#Mano del casino

print("La mano del casino:", end=" ")
carta_casino1 = choice(lista_baraja)
score_casino1 = baraja[carta_casino1]
print(carta_casino1, end=" ")
carta_casino_oculta = chr(0x1f0a0)
print(carta_casino_oculta, end=" ")
print("La puntuación del casino es de: ", score_casino1)

#Con la siguiente función le daremos la opción al jugador de elegir una posible tercera carta., la banca revelara su mano y, finalmente, se elegirá al ganador

def pedir_tercera_carta ():
    opcion = int(input("Introduce 1 si quieres otra carta, si no 2: "))
    while opcion < 1 or opcion > 2:
        print("Error introduzca 1 o 2: ")
        opcion = int(input("Introduce 1 si quieres otra carta, si no 2: "))
        break
    if opcion == 1:
        carta_jugador3 = choice(lista_baraja)
        score_jugador2 = score_jugador + baraja[carta_jugador3]
        print("Sus cartas son: ", carta_jugador1, carta_jugador2, carta_jugador3, end=" ")
        print("Su nueva puntuación es de: ",score_jugador2)

        if score_jugador2 > 21:
            print("La banca gana")
        else:
            print("La mano del casino es: ", end=" ")
            carta_casino2 = choice(lista_baraja)
            score_casino2 = score_casino1 + baraja[carta_casino2]
            print(carta_casino1, carta_casino2)
            print("La puntuación del casino es de: ", score_casino2)

            if score_casino2 < 14:  
                carta_casino3 = choice(lista_baraja)
                score_casino2 = score_casino2 + baraja[carta_casino3]
                print("Las cartas del casino son: ", carta_casino1, carta_casino2, carta_casino3)
                print("La puntuación del casino es: ", score_casino2)
                if score_casino2 > 21:
                    print("Ganaste")
                else:
                    while score_jugador2 != score_casino2:
                        if score_jugador2 > score_casino2:
                            print("Ganaste")
                        if score_jugador2 < score_casino2:
                            print("La banca gana")
                        else:
                            print("Empate, no hay ganador")
                        break
                
    if opcion == 2:
        print("Sus cartas son: ", carta_jugador1, carta_jugador2)
        print("Su puntuación es de: ", score_jugador)

        if score_jugador > 21:
            print("La banca gana")
        else:
            print("La mano del casino es: ", end=" ")
            carta_casino2 = choice(lista_baraja)
            score_casino2 = score_casino1 + baraja[carta_casino2]
            print(carta_casino1, carta_casino2)
            print("La puntuación del casino es de: ", score_casino2)
            if score_casino2 < 14:  
                carta_casino3 = choice(lista_baraja)
                score_casino2 = score_casino2 + baraja[carta_casino3]
                print("Las cartas del casino son: ", carta_casino1, carta_casino2, carta_casino3)
                print("La puntuación del casino es: ", score_casino2)
                if score_casino2 > 21:
                    print("Ganaste")
                else:
                    while score_jugador != score_casino2:
                        if score_jugador > score_casino2:
                            print("Ganaste")
                        if score_jugador < score_casino2:
                            print("La banca gana")
                        else:
                            print("Empate, no hay ganador")
                        break


opcion = pedir_tercera_carta()