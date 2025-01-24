import timeit, random


data = [random.randint(1,1000) for x in range(100_000)]

def get_min(data):
    min_value = data[0]

    for value in data:
        if value < min_value:
            min_value = value

    return min_value

def test1():
    get_min(data)

def test2():
    min(data)

print(timeit.timeit(test1, number=1_000))
print(timeit.timeit(test2, number=1_000))

