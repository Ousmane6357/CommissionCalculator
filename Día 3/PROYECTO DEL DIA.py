texto_de_usuario=(input("Usuario introduce un texto: "))
letra = []
texto_de_usuario=texto_de_usuario.lower()
print((texto_de_usuario))

print(" Ahora introduce tres letras, sigue el orden para ingresar tus letras")

l1 = input(str("Introduce la primera letra: "))
lista1 =[l1]
lis1 = l1.lower()
print("La cantidad de la primera letra en el texto es : ")

l2 = input(str("Introduce la segunda letra: "))
lista2 =[l2]
lis2 = l2.lower()

l3 = input(str("Introduce la tercera letra: "))
lista3 =[l3]
lis3 = l3.lower()


print("Tu texto es: "+ texto_de_usuario + " las letras que elegiste son:\n "+l1 + l2 + l3+" y la cantidad de letras que contiene tu texto es : ")
print(len(texto_de_usuario))

print("La primera y última letras de tu texto son : ")
primera_ultima_letras = texto_de_usuario.index()
print(primera_ultima_letras)









