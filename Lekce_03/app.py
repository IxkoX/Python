# app.py

from users import login, register

while True:
    username = input('Zadej username: ')
    password = input('Zadej heslo: ')
    success = login(username, password)
    if success:
        print('OK')
        break
    else:
        print("Invalid")