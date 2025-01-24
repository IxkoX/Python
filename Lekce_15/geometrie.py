# geometrie.py

def get_triangle_perimeter(a, b, c):
    resolut =  a + b + c
    return resolut

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def get_square_area(a):
    if a <= 0:
        raise ValueError('strana musí být kladná')
    
    return a * a