archivo = open('Prueba.txt' , 'w')

archivo.write('Soy el nuevo texto que viene a remplazar todo\n')

archivo.writelines('Nuevo inicio de session')
archivo.close()