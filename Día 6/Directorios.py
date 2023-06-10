from pathlib import Path

carpeta = Path('/Users/ousmanedagnogo/Documents/AUTODIDACTO/PYTHON/')


archivo = carpeta / 'Otro.txt'


mi_archivo = open(archivo)

print(mi_archivo.read())