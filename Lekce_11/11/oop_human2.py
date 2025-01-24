# oop_human2.py

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
    
    def __repr__(self):
        """ reprezentace v listu """
        return self.name + ' ' + str(self.age)

    def add_friend(self, human):
        self.friends.append(human)


petr = Human('Petr', 30)
alex = Human('Alex', 20)
dana = Human('Dana', 23)

petr.add_friend(alex)

alex.friends.append(petr)
alex.friends.append(dana)
dana.friends.extend([petr, alex])

print(petr.friends)
print(alex.friends)
print(dana.friends)