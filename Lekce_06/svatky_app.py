# svatky_app.py

import json

with open('Lekce_05/svatky.json', encoding='utf8') as file:
    data = json.load(file)
    print(data['0410'])


def find_day(name):
    for key, value in data.items():
        if name in value:
            return key
            


print(find_day('Petr'))
