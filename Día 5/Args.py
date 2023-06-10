def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma(5,6,5,8,500))




#Otra forma
def suma(*args):
    return sum(args)
print(suma(5,6,7,34,67,865,34454))




#Ejercicio
def numeros_personas(*args):
    nombre = 'Ousmane'
    suma_numeros = 0
    for num in args:
        suma_numeros += num
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje
resultado = numeros_personas(1,2,4,5,67,3)
print(resultado)