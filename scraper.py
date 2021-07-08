import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = 'https://www.ivalor.com.br'
webpage = requests.get('https://www.ivalor.com.br/empresas/listagem?p=1').content

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


bLinks = []
for x in aLinks:
    print(x.get('href'))





# print(table_row)
# links = []
# for links in table_data:
#     links.append(prefix + str(links.get('href')))

# links = []
# for link in soup.find_all('a'):
#     links.append(prefix + str(link.get('href')))

# companies = []
# for link in links:
#     for word in link:
#         if word.isupper():
#             companies.append(link)

# print(links)