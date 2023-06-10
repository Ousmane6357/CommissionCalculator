from random import *


# Lista inicial
palitos = ['-','--','---','----']


#Mezclar a los palitos
def mezclar(lista):
    shuffle(lista)
    return (lista)



#Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)



#Comprobar el intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")



palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


#Mi pratica
import random

def lanzar_dados():
    resultado_dado1 = random.randint(1, 6)  # Generar un número aleatorio entre 1 y 6
    resultado_dado2 = random.randint(1, 6)  # Generar otro número aleatorio entre 1 y 6
    return resultado_dado1, resultado_dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Ejemplo de uso
resultado_dado1, resultado_dado2 = lanzar_dados()
mensaje = evaluar_jugada(resultado_dado1, resultado_dado2)
print(mensaje)












