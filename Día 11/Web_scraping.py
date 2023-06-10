import bs4
import requests

resultado = requests.get('https://www.estrategiasdeinversion.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

columna_lateral =  sopa.select('.masthead a')
for p in columna_lateral:
    print(p.get_text())


