import bs4
import requests


url_base= 'http://books.toscrape.com/catalogue/page-{}.html'

resultados = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultados.text, 'lxml')

print(len(sopa.select('.product_pod')))