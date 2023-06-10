precios_de_cafe = [('capuchino',1.50),('Express',1.20),('Moka',1.9)]
for elemento in precios_de_cafe:
    print(elemento)




precios_de_cafe = [('capuchino',1.50),('Express',2.20),('Moka',1.9)]
for cafe,precio in precios_de_cafe:
    print(precio * 0.45)






# cafe más caro
precios_de_cafe = [('capuchino',2.50),('Express',3.20),('Moka',1.9)]
def cafe_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro= ''

    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)
print(cafe_mas_caro(precios_de_cafe))



#Otra forma de hacer
precios_de_cafe = [('capuchino',2.50),('Express',3.20),('Moka',5.9)]
def cafe_mas_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro= ''

    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)
cafe, precio = cafe_mas_caro(precios_de_cafe)
print(f"El cafe màs caro es {cafe} cuyo precio es {precio}")