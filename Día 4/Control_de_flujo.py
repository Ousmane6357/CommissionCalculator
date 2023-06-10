
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1}  no es mayor que {num2}")


if num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num2} no es mayor que {num1}")



if num1 == num2:
    print(f"{num1} y {num2} son iguales")
else:
    print(f"{num1} y {num2} no son iguales")



edad = int(input("Introduce tu edad: "))
tiene_licencia = False

if edad >=18:
    print("Puedes conducir")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
if edad <18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")






