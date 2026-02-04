import requests
import re
from bs4 import BeautifulSoup

def remover_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def get_app_details(app_id):

    URL_BASE = f'https://store.steampowered.com/api/appdetails?appids={app_id}'

    r = requests.get(URL_BASE)

    minimum_req = r.json()[f'{app_id}']['data'].get('pc_requirements', 'None')['minimum']
    
    teste = remover_html(minimum_req)

    teste1 = re.search(r'(Memory:).*?(\d+.*?GB)', teste)

    return teste1.group(1,2)
# teste1.group(1, 2)

lista = [
    20900, 65930, 203160, 203680, 209080, 218620, 231430, 238320, 
    242700, 269210, 292030, 304050, 359550, 368420, 424840, 431960, 552500, 
    582660, 623990, 706220, 899770, 1063730, 1180660, 1422450, 1619990, 
    1808500, 2149010, 2694490, 2920570
]

lista_result = []
for i in lista:
    try:
        lista_result.append((get_app_details(i)))
    except:
        print('esse n entrou', i)


print(lista_result)

