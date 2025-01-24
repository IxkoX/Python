import json, time
import datetime
import requests


def generate_urls():
    d = datetime.date(2000, 1, 1) # datum 1.1.2000
    url = 'https://svatky.adresa.info/json?date='
    url_data = []
    
    for number in range(366): #366
        date = d + datetime.timedelta(days=number)
        dm = date.strftime('%d%m')
        url_data.append(url + dm)

    return url_data

def get_data(url):
    """
    1. pošle požadavek na url
    2. zpracuje odpověď - na json
    3. vrátí data
    """
    response = requests.get(url)
    #time.sleep(0.5)
    data = response.json()
    return data



urls = generate_urls()
all_data = {}

for url in urls:
    json_data = get_data(url)
    
    for item in json_data:
        key = item['date'] #0101
        value = item['name'] #kamila

        if key not in all_data:
            all_data[key]= []
        
        all_data[key].append(value)

# print(all_data)

with open('Lekce_05/svatky.json', mode='w', encoding='utf-8') as file:
    json.dump(all_data, file)


