data = ['Jan', 'Petr', 'Nina']

result = []

for item in data:
    result.append(item[0].lower())

print(result)

# list comprehension
# generátorová notace
result2 = [x[0] for x in data]

print (result2)

d = {'A':1, 'B':2}

d2={d[key] :key for key in d}
print(d2)
print(type(d2))