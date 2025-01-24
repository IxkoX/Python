# geom.py
import math

def get_circle_length(radius):
    result = 2 * math.pi * radius
    return round(result, 2)

def get_circle_area(radius):
    result = 3.14 * math.pi ** 2
    return round(result, 2)


def test(a, b, c, key=100):
    print(a, b, c, key)

test(1, 2, 3)
test(1, 2, 3, key=10)

def get_icecream(volume, flavour='Vanilka'):
    print(f'{flavour} Icecream {volume}')

get_icecream(100)
get_icecream(100, flavour='Chocolate')
get_circle_length(10)
print(math.pi)
