def chequear_3_cifras(numero):
    return numero in range(100,1000)
suma = 344 + 430
resultado= chequear_3_cifras(suma)
print(resultado)





def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return  True
        else:
            pass

    return False
resultado = chequear_3_cifras([55,99,6000])
print(resultado)




def chequear_3_cifras(lista):
    lista_3_cifras= []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras
resultado = chequear_3_cifras([505,99,600])
print(resultado)




def todos_positivos(numeros):
    for lista_numeros in numeros:
        if lista_numeros < 0:
            return True
        else:
            return False





def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador += 1
    return contador






