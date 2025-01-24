# identifikacni_funkce.py

class Car:
    def __init__(self):
        self.name = 'Super car'

    def __eq__(self, other):
        return self.name == other.name

    def info(self):
        print('call inf', self)

class SportCar(Car):
    pass


car = Car()
sport_car = SportCar()

print(car == sport_car)

print("-" * 20, 'id', "-" * 20)
print(id(car))
print(id(sport_car))

print("-" * 20, 'type', "-" * 20)
print(type(car))
print(type(sport_car))
print(type(car) is Car)
print(type(sport_car) is Car)

print("-" * 20, 'isinstance', "-" * 20)
print(isinstance(sport_car, Car))
print(isinstance(sport_car, SportCar))
print(isinstance(sport_car, (SportCar, int)))

print("-" * 20, 'vars', "-" * 20)
print(vars(car)) #dict atributů a hodnot

print("-" * 20, 'dir', "-" * 20)
print(dir(car)) # názvy atributů a metod
print(car.__class__.__name__)

print("-" * 20, 'getattr, hasattr, setattr, delattr', "-" * 20)
setattr(car, 'power', 100)
print(hasattr(car, 'power'))

