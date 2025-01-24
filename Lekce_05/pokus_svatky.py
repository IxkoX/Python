import requests
from datetime import date, timedelta

# Začátek a konec roku
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

# Iterace přes všechny dny
current_date = start_date
while current_date <= end_date:
    # Formátování data do tvaru ddmm
    formatted_date = current_date.strftime('%d%m')
    # Vytvoření URL s aktuálním datem
    url = f'https://svatky.adresa.info/json?date={formatted_date}'
    print(f"Fetching: {url}")
    
    # Volání API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Zvedne chybu, pokud HTTP odpověď není 200
        data = response.json()
        print(data)  # Zpracujte data podle potřeby
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {formatted_date}: {e}")
    
    # Posun na další den
    current_date += timedelta(days=1)
