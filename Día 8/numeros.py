def numero_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"


def numero_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"


def numero_comestica():
    for n in range(1,10000):
        yield f"C - {n}"


p = numero_perfumeria()
f = numero_farmacia()
c= numero_comestica()



def decorador(rubro):
    print('\n' + '*' * 30)
    print("Su número es:")
    if rubro == 'P':
        print(next(p))

    elif rubro == 'F':
        print(next(f))

    else:
        print(next(c))
    print("Espere y sera atendido")
    print('*' * 30 + '\n')