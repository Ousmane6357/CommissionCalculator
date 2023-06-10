from collections import namedtuple
from collections import Counter
from collections import defaultdict



#ejercicio namedtuple
persona = namedtuple('Persona',['nombre','altura','peso'])
persona('Ousmane', 1.34, 434)
personaje= persona('Ousmane',1.78,80)
print(personaje[1])


#Ejercicio de Counter
numeros = [5,6,7,7,4,3,6,7,8,5,8,9,9,]
print(Counter(numeros))

frase = 'el pan pan y vino vino'
print(Counter(frase.split()))

serie = Counter([1,2,2,3,4,5,6,6,4,4,6,8,8,9])
print(serie.most_common(1))
print(serie.popitem())

mi_dic = {'Uno':'verde','dos':'azul','tres':'rosa'}
print(mi_dic['dos'])

diccionario = defaultdict(lambda : 'nada')
diccionario['uno'] = 'verde'
print(diccionario['cuatro'])



