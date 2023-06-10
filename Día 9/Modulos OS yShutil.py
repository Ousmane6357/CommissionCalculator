import os
import shutil
import send2trash



#manipular archivo
archivo = open('curso.text', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

#Desplazar archivos
shutil.move('curso.text',"Users/ousmanedagnogo/Documents")


#Eliminar archivo
