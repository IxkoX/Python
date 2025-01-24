# oop_1.py

# třída vs instance

class Human:
    def __init__(self, name, age, best_friend=None):
        print("Create Human")
        self.name = name
        self.age = age
        self.best_friend = best_friend

    def introduce(self):
        print(f"Hello my name is {self.name} and I am {self.age}")
    
    def rename(self, new_name):
        self.name = new_name
    
    def get_older(self):
        """ tato metoda zvýší věk o 1 """
        self.age = self.age + 1


suche = Human("Suche", 34)
karel = Human("Karel", 28, suche)
leos = Human("Leoš", 28, suche)

print(karel.best_friend.age)
print(leos.best_friend.age)
leos.best_friend.name = 'XYZ'
print(leos.best_friend == karel.best_friend) # False / True

suche.introduce()
karel.introduce()

karel.rename("Jakub")
karel.get_older()




