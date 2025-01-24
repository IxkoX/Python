# functional_map.py

data = [2, 8, 9]

# pomocí list comprehension zjistit druhou mocninu [4, 64, 81]
squares = [x**2 for x in data]

print(squares)

result = map(lambda x: x**2, data)
print(list(result))