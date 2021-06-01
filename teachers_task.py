'''
https://zaochnik.com/spravochnik/pravo/teorija-gosudarstva-i-prava/slovar-osnovnyh-juridicheskih-terminov/
 собери все юр. термины с этого сайта,
 сохрани в .json либо .csv
'''

from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {

    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    'Accept-Language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

site_head = 'https://zaochnik.com/'
url = 'https://zaochnik.com/spravochnik/pravo/teorija-gosudarstva-i-prava/slovar-osnovnyh-juridicheskih-terminov/'


req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.content, 'lxml')
#print(soup.prettify())

ur_termin = soup.select('div.article__content.theme p')
ur_termin = [i.text for i in ur_termin]
#print(ur_termin)
# обрезать ничего не надо,вывод терминов корректен

ur_termin = {'termin': ur_termin}
#ur_termin_json.append(ur_termin)

with open('ur_termin_2.json', mode='w', encoding='utf-8') as u:
    json.dump(ur_termin, u, indent=4, ensure_ascii=False)




