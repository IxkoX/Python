# web_scraping.py

import re
import requests
import json


pattern = r'<div class="inzeratynadpis">\s*<a href="(.*?)">\s*<img src="(.*?)" class="obrazek" alt="(.*?)"'
rx_bazos = re.compile(pattern)
url = 'https://mobil.bazos.cz/'

response = requests.get(url)

result = rx_bazos.findall(response.text)

data = []
for url, img, title in result:
    item = {'url': url,'img': img,'title': title,}    
    data.append(item)
    
    # jiný zápis:
    # data.append({
    #     'url': url,
    #     'img': img,
    #     'title': title,
    # })
with open ('Lekce_08/data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
