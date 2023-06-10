nombres = ['Ousmane','Aware','Charlene']
edades =[22,33,19]
ciudades = ['Abidjan','Bamako','Lome']

combinados = list(zip(nombres,edades,ciudades))
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}  ")




capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinaciones = list(zip(capitales,paises))
for capital,pais in combinaciones:
    print(f"la capital de {pais} es {capital}")




numeros = list(zip(['uno', 'dos', 'tres', 'cuatro', 'cinco'],
                   ['um', 'dois', 'três', 'quatro', 'cinco'],
                   ['one', 'two', 'three', 'four', 'five']))

print(numeros)