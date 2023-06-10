lista = ['Ousmane','Dagnogo','Aware']
for indice,item in enumerate(lista):
    print(indice,item)




lista = ['Ousmane','Dagnogo','Aware']
for item in enumerate(lista):
    print(item)



lista = ['Ousmane','Dagnogo','Aware']
mis_tuples = list(enumerate(lista))
print(mis_tuples[1])



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for numerador in list(enumerate(lista_nombres)):
    print(f"{numerador} se encuentra en el indice {numerador[:-1]}")



palabra= "Python"
lista = list(enumerate(palabra))
lista_indices = lista
print(lista)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for empezar in lista_nombres:
    if empezar.startswith('M'):
        print(empezar)