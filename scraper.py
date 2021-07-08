import requests
from bs4 import BeautifulSoup
import pandas as pd

count = 0
bLinks = []
for r in range(0, 25):
    count += 1

    prefix = 'https://www.ivalor.com.br'
    preurl = 'https://www.ivalor.com.br/empresas/listagem?p='
    url = preurl + str(count)
    webpage = requests.get(url).content

    soup = BeautifulSoup(webpage, 'html.parser')


    links = []
    datas = []
    table_body = soup.find(id='tab_empresas_body')
    rows = table_body.findAll('tr')
    for tr in rows:
        datas.append(tr.find_all('td')[2].find_all('a'))

    aLinks = []
    for data in datas:
        aLinks.append(data[0])



    for x in aLinks:
        bLinks.append(prefix + x.get('href'))

for link in bLinks:
    webpage = requests.get(link).content
    soup = BeautifulSoup(webpage, 'html.parser')
    p = soup.find_all("p", {"class": "texto-claro"})
    contador = 0
    for x in p:
        if contador <= 7:
            print(x.text)
            contador += 1
    print('.....................................................')
    print('.....................................................')
    print('.....................................................')


