import requests
from bs4 import BeautifulSoup as bs


url = 'https://portal.ifrn.edu.br/'

response = requests.get(url)

page = bs(response.text, 'html.parser')

noticias = page.find_all('span', {'class':"news_title"})

for noticia in noticias:
	print(noticia.text+'\n')