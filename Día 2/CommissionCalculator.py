nombre = input("¿Introduce tu nombre?: ")
ventas = input("¿Cuanto has vendido?: ")


print("Hola " + nombre+ " Has vendido " + ventas)
ventas = int(ventas)

comission = ventas * 13 / 100
comission = round(comission,2)
print(f"El sueldo que combraras es {comission}")




nombre = input("Introduce tu nombre?: ")
ventas = int(input("Cuanto has vendido?: "))

comission = round(ventas * 13 / 100,2)

print(f"Hola {nombre} has vendido {ventas} y el sueldo que cobraras sería {comission}")






