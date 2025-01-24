# team.py

class Company:
    def __init__(self, name: str):
        self.name = name

class Team:
    def __init__(self, name: str, company: Company):
        self.name = name
        self.company = company
        self.members = set()
    
    def __str__(self):
        return self.name
    
    def add_member(self, employee: 'Employee' ):
        employee.set_team(self)
        self.members.add(employee)
    
    def remove_member(self, employee: 'Employee'):
        self.members.remove(employee)


class Employee:
    def __init__(self, name: str, team: Team = None):
        self.name = name
        self.team = team
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def set_team(self, new_team):
        if self.team:
            self.team.remove_member(self)

        self.team = new_team

if __name__ == '__main__':
    it_security = Company('IT Guards s.r.o')
    it_security2 = Company('IT Guards2 s.r.o')
    it_security4 = Company('IT Guards3 s.r.o')
    it_security5 = Company('IT Guards4 s.r.o')

    team1 = Team("Development", it_security)
    team2 = Team("Marketing", it_security2)

    franta = Employee("Franta Vomáčka")
    maruska = Employee("Maruška Pěkná")
    tomas = Employee("Tomáš Strouhal", team2)

    print(franta.team)
    print(team1.members)

    team1.add_member(franta)

    print(franta.team)
    print(team1.members)

    team1.add_member(maruska)

    print(maruska.team)
    print(team1.members)

    team2.add_member(maruska)
    print(maruska.team)
    print(team2.members)
    print(franta.team)
    print(team1.members)


