import bs4
import requests

#crear url sin numero de pagina
url_base= 'http://books.toscrape.com/catalogue/page-{}.html'

# lista de título de 4 o 5 estrellas
titulo_rating_alto= []

#iterar pagina
for pagina in range(1,51):


    #Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #selecionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:

        #chequear que tenga 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')):

            # Guardar titulo en variable
            titulo_libro =libro.select('a')[1]['title']

            #agreagar libro a la lista
            titulo_rating_alto.append(titulo_libro)

#ver los libros de 4 y 5 estrellas en panatalla
for t in titulo_rating_alto:
    print(t)