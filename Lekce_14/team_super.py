# team_super.py

from team import Company, Team, Employee

class SuperTeam(Team):
    def add_member(self, employee: 'Employee'):
        if type(employee) != SuperEmploye:
            raise TypeError('eployee must be instance of Employee')
        
        super().add_member(employee)

        

class SuperEmploye(Employee):
    pass

marvel = Company('Marvel')
super_team_1 = SuperTeam('Avangers', marvel )

print(super_team_1)

thor = SuperEmploye('Thor')
super_team_1.add_member(thor)

print(thor.team)
print(super_team_1.members)
