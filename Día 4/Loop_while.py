moneda = 5
while moneda > 0:
    print(f"Tengo {moneda} monedas")
    moneda -=1
else:
    print("Se me acabó la pasta")




respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir (s/n)")
else:
    print("Gracias")




numero = 10
while numero >1:
    numero -=1
    print(f"tengo {numero}")
else:
    print("No me queda nada")



numero = 51
while numero >0:
    numero -= 1
    print(numero)




lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for elemental in lista_numeros:
    print(elemental)
    if elemental < 0:
        break




