from django.http import HttpResponse
from django.shortcuts import render
import random
import datetime as dt

def index_page(request):
    print(request.method)
    print(request.path)
    
    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f'''
                        <h1>Hello From Django: {number} | {d}</h1>
                        <img src="https://picsum.photos/200/300">
                        ''')


"""
úkol: vytvořte zde view s názvem time_page
pamatujte: na vstupu musí být request a na výstupu HttpResponse
"""
def url_paths(requests):

    print(requests.GET)
    print(requests.GET['xyz'])
    print(requests.GET.getlist('xyz'))

    return HttpResponse('This page is working')

def my_math(request):

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']

    if operation == 'plus':
        result= a + b
    elif operation == 'minus':
        result= a-b
    elif operation == 'ultiple':
        result= a*b
    elif operation == 'divide':
        result= a/b
    return HttpResponse(f'RESULT: {result}')

def test_template(request):
    name = request.GET.get('name', 'World')
    age = request.GET.get('age', '0')
    if age == '':
        age = 0

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'age' : age
    }

    return render(request, 'test_template.html', context)

def calculator(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a+b
    except (KeyError, TypeError):
        result= ''
    
    context = {
        'result': result
    }


    return render(request, 'calculator.html', context)