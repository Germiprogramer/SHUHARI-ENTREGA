from random import choice, sample
#choice te elige 2 cartas al azar, sample te muestra las dos cartas que has elegido
#keys, values
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

#sample = barajar

print("Cartas: {}". format(" ".join(cartas.keys())))
print("Puntos: {}". format(list(cartas.values())))

#print("1\ Iteración estándar sobre un diccionario")
print("Presentación de las cartas del juego y sus distintos valores:")

for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta,valor))

#print("2\ Iteración ordenada sobre un diccionario")
#for carta in sorted(cartas.keys()):
    #print("la carta {} vale {}".format(carta,cartas[carta]))

print("3\ Black Jack")
lista_cartas = list(cartas)
#Sacamos las dos primeras cartas del jugador
print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")

print(">>> su puntuación es de", score , "puntos")

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
#print("La banca tiene: {} {} >> su puntuación es {}".format(main_banca[0], main_banca[1], score_banca))

if score_banca < 17:
    cartabanca = choice(lista_cartas)
    score_banca = score_banca + cartas[carta]
    print("la banca coge otra carta")

def comparar():
    if score == 21 and score > score_banca:
        print("Has ganado")
    elif score == 21 and score == score_banca:
        print("Empate técnico mister")
    else: 
        seguirjugando = input("¿Quieres coger otra carta?   si/no:    ")


    if seguirjugando == "no":
        print("La banca tiene: {} {} >> su puntuación es {}".format(main_banca[0], main_banca[1], score_banca))
        if 22 > score_banca > score:
            print("Has perdido :(")
        elif score > score_banca:
            print("Has ganado :)")
        else:
            print("empate técnico")
        

    if seguirjugando == "si":
        carta = choice(lista_cartas)
        newscore = score + cartas[carta]
        print(carta, end=" ")
        print(">>> su puntuación es de", newscore , "puntos")
        print(">>> el score de la banca es de", score_banca, "puntos")
            
        if newscore > 21 or newscore < score_banca < 22:
            print("has perdido")
        elif 21 >= newscore > score_banca:
            print("has ganado")
        elif newscore and score_banca > 21:
            print("banca y jugador han superado los 21, por tanto empate")
        
       
comparar()
