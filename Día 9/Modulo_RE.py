import re

texto = 'llama al 456-654-355 ya mismo'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{3})')

resultado = re.search(patron, texto)

print(resultado.group(1))



#Cuantificadores
info ='No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', info)

print(buscar)