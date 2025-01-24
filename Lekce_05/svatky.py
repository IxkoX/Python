# svatky.py

import time, requests, datetime

url ='https://svatky.adresa.info/json?date=2412'

response = requests.get(url)

print(response) 
data = response.json()
print(data)