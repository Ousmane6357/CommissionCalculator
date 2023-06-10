import bs4
import requests

resultado = requests.get('https://www.estrategiasdeinversion.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.photo')[0]['data-src']
print(imagenes)

imagen_curso = requests.get(imagenes)

f =open('mi-imagen.jpg', 'wb')

f.write(imagen_curso.content)
f.close()


