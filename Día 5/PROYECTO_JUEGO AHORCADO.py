import random
from random import *

#Palabra al azar
palabras = ['a','h','y','x']
aleatorio = choice(palabras)
print("La cantidad de nuestra palabra es: 4, por lo tanto ['-','--','---','----']")


#Que elija el usuario
intentos = 0
estimado = 0
usuario = input("Elige una letra: ")
while intentos <8:
    estimado= input("Elige otra letra: ")
    intentos += 1

    if intentos > 8:
        print("Has perdido el juego")


    while estimado not in palabras:
        estimado = input("Vuelve a intentar: ")
        if estimado == aleatorio:
            print("Has ganado")
    else:
        print("Vuelve a intentar")










