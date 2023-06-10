lista = ['Ousmane','Mamadou','Adja','Batoman']
for saludo in lista:
    print("Hola " + saludo)




lista = ['Ousmane','Mamadou','Adja','Batoman']
for elemento in lista:
    numero_de_letras = lista.index(elemento) +1
    print(f"El nombre numero {numero_de_letras} : es {elemento}")




lista_de_clase = ['Fede','Aicha','Estelle','Issouf']
for elemento in lista_de_clase:
    contador = lista_de_clase.index(elemento) +1
    print(f"el nombre {contador} es : {elemento}")




amigos = ['Mireille','Dosso','Charlène','Sally']
for elemento in amigos:
    if elemento.startswith('C'):
        print(elemento)




numeros = [100,200,300,400]
mi_valor = 0
for elemento in numeros:
    mi_valor = mi_valor + elemento
print(mi_valor)


palabra = 'Python'
for elemento in palabra:
    print(elemento)



dic = {'clave1':'a','clave2':'b','clave3':'c',}
for item in dic.items():
    print(item)



alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for elemento in alumnos_clase:
    print("Hola " +elemento)





lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0
for elemento in lista_numeros:
    suma_numeros = suma_numeros + elemento
print(suma_numeros)




lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num %2 == 0:
       suma_pares += num
    else:
        suma_impares += num


print(f"La suma de los numeros pares son :  '{suma_pares}'")
print(f"La suma de los numeros pares son :  '{suma_impares}'")




