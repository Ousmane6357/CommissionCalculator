from random import *

intentos =0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Introduce tu nombre: ")

print(f"Bueno {nombre} he pensado un numero entre 1 y 100\nTienes 8 intentos")

while intentos <8:
    estimado = int(input("Cual es el numero?: "))
    intentos +=1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va desde 1 a 100")

    elif estimado < numero_secreto:
        print("Mi numero es màs alto")

    elif estimado > numero_secreto:
        print("Mi numero es màs bajo")

    else:
        print(f"Felicitaciones '{nombre}' has adivinado el numero al intento numero{intentos}")
        break

if estimado != numero_secreto:
    print(f"Lo siento {nombre} se han agota los intentos\n el numero secreto era{numero_secreto}")