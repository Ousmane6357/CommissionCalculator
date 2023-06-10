texto = input("Ingresa un texto a eleccion: ")
letras = []
texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRA")
cantida_de_letras1 = texto.count(letras[0])
cantida_de_letras2 = texto.count(letras[1])
cantida_de_letras3 = texto.count(letras[2])

print(f"hemos encontrado la letra '{letras[0]}' repetida {cantida_de_letras1} veces")
print(f"hemos encontrado la letra '{letras[1]}' repetida {cantida_de_letras2} veces")
print(f"hemos encontrado la letra '{letras[2]}' repetida {cantida_de_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"hemos encontrado {len(palabras)} palabras en tu texto")


print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO AL INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir : '{texto_invertido}'")

print("\n")
print("BUSCAR LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"si" , False:"no"}
print(f"La palara 'python' {dic[buscar_python]} se encuentra en el texto")