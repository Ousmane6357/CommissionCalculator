

texto = "Este es mi texto "
resultado= texto.replace('texto', 'avion')

print(resultado)


a = "Abidjan"

b = "Est"

c= "Doux"

d= "-".join([a,b,c])
print(d)


frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

resultado = frase.upper()
print(resultado)

lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)


frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace('difícil','fácil')
resultado1 = frase.replace('mala','buena')
print(resultado)
