# files.py
# práce se soubory

def read():
    with open('Lekce_04/soubor.txt', mode='r', encoding='utf-8') as file:
    # text = file.readline()
    # print(text)¨
        for line in file:
            print(line)


def write():
    with open('Lekce_04/test.txt', mode='w', encoding='utf-8') as file:
        file.write('HELLO FROM PYTHON')

def append():
    with open('Lekce_04/test2.txt', mode='a',encoding='utf-8' ) as file:
        file.write("Nový obsah na konec souboru.\n")

append()
write()
#read()