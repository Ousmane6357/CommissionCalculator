lista = print([letra for letra in 'Python' ])



lista1 = print([x for x in range(0,51,5) ])



lista2 = print([y/5 for y in range(0,51,5) ])



lista3 = print([x for x in range(0,51,5)  if x * 2 > 10])



lista4 = print([ x if x * 2 > 10 else 'no' for x in range(0,51,5)])



pies = [10,20,30,40,50]
metros = [p* 3.281 for p in pies]
print(metros)



pies1 = [10,20,30,40,50]
metros1 = [p / 3.281 for p in pies]
print(metros1)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numero ** 2 for numero in valores]
print(valores_cuadrado)



valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [ numero for numero in valores if numero % 2 == 0]
print(valores_pares)



temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temperatura - 32) * (5/9) for temperatura in temperatura_fahrenheit]

print(grados_celsius)

