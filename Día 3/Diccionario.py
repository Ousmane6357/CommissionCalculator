diccionario = {'c':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)


cliente = {'nombre':'Ousmane', 'apellido':'Dagnogo','edad':'23', 'talla':'1.79'}
consulta = (cliente['apellido'])
print(consulta)



coche = {'marca':'AUDI','color':'Amarillo', 'antiguedad':2020}
consulta1 =  (coche['color'])
print(consulta1)




mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':'35','ocupacion':'Periodista'}
print(mi_dic['edad'][0:3])



mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])