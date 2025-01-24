# user.py

import os, json, hashlib


DATA_PATH = 'Lekce_03/users.json'

def hash_password(password):
    hash_value = hashlib.sha256(password.encode())
    return hash_value.hexdigest()

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)
    
def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) #zapiš to do json

def register(username, password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')
    
    # Takhle neotvírat soubory ke čtení
    # file = open(DATA_PATH, encoding='utf-8')
    # print(file.read())
    # file.close()
    
    # Ale takto ano - pomocí with - což je kontextový manažer
    
    data = read_data()

    if username in data:
        raise ValueError('Uživatel již existuje')
        
    data[username] = password
    data = write_data(data)

    # Toto jsme ud2lali univerzalni do samostatne funkce
    # with open(DATA_PATH, mode="w", encoding='utf-8') as file:
    #     json.dump(data, file) #zapiš to do json
    

def login(username, password):
    pass

def logout(username):
    pass

def change_password(old_password, password, password_repeat):
    pass


register('test', 'heslo', 'heslo')

