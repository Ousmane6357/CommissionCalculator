import bs4
import requests


url_base= 'http://books.toscrape.com/catalogue/page-{}.html'

resultados = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultados.text, 'lxml')

libros= sopa.select('.product_pod')

ejemplo= libros[0].select('a')[1]['title']
print(ejemplo)