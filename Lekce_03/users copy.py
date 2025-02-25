# users copy.py

import os, json, hashlib

DATA_PATH = 'Lekce_03/users.json'

def hash_password(password):
    # hashlib.sha256(password.encode()).hexdigest()
    hash_value = hashlib.sha256(password.encode())
    return hash_value.hexdigest()

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)
    
def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) #zapiš to do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')
    
def check_username(data, username):
    if username in data:
        raise ValueError('Uživatel již existuje')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username) 
    data[username] = hash_password(password)
    write_data(data)

def login(username, password):
    data = read_data()
    try: 
        assert data[username] == password, 'Chybné heslo'
        return True
    except (KeyError, AssertionError):
        return False

def logout(username):
    pass

def change_password(old_password, password, password_repeat):
    pass

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)


#register('test4', 'heslo', 'heslo')
# print(login('tes', 'heslo'))
# delete_user('test4','heslo')
def test2():
    register('test4','heslo','heslo')

test2()