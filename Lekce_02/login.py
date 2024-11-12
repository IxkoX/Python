data = {
    "Jakub" : "heslo1",
    "Jana" : "heslo2",
    "Petr" : "heslo3",
    "Jirka" : "heslo4"

}

username = input("Zadejte username: ")
password = input("Zadejte heslo: ")
"""
if username in data and password == data[username]:
        print("OK")
else:
    print("přihlášení se nepodařilo")
"""

try:
    assert data[username] == password
    print("OK")
except:
    print("přihlášení se nepodařilo")