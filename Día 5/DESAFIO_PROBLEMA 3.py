#Escribe una función que requiera una cantidad indefinida de argumentos.
# Lo que hará esta función es devolver True
# si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.

def ceros_vecinos (*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):

            return False

        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False

print(ceros_vecinos(5,6,6,6,6,6,6,4,4,0,4,0,0,2,2))