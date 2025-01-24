# functional.py

data = ['Petr', 'Jan', 'Nina']

data.sort(key=len)
print(data)

data.sort(key=lambda x: x[-1])

print(data)

data.sort(key=lambda x: (len(x), x))

print(data)