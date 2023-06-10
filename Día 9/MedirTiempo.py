import timeit


declaracion = '''
prueba_for
'''

setup = '''
    def prueba_numero(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)

    return lista
'''


duracion = timeit.timeit(declaracion, setup, number=100000)
print(duracion)


declaracion2 = '''
prueba_while(10)
'''

setup2 = '''
def prueba_while(number):
    lista = []
    contador = 1
    while contador <= number:
        lista.append(contador)
        contador += 1
    return lista

'''

duracion2 = timeit.timeit(declaracion2, setup2, number=10000)
print(duracion2)