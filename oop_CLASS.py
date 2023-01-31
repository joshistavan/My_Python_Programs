# class student:
#     pass
# stavan=student
# kano=student
# stavan.std='collageboy'
# kano.list=[1,'sta',44]
# print(stavan,kano.list)

# class employ:
#     no_of_leave=10
#     pass
# stavan=employ
# kano=employ
# stavan.salary=100000
# kano.salary=200000
# stavan.role='bhai'
# kano.role='python developer'
# print(kano.role,stavan.role, employ.no_of_leave)
# print(stavan.__dict__)
# stavan.no_of_leave=15
# print(employ.no_of_leave)
# print(stavan.__dict__)

#-----------------self example------------------------
# class employee:
#     def printdetail(self):
#         return f'salary is{self.salary}. favourite is {self.favourite} and role is {self.role}'
# stavan=employee()
# kano=employee()
#
# stavan.salary=100000
# stavan.role='student'
# stavan.favourite='jai Bhole'
#
# kano.salary=200000
# kano.role='Shiv Bhakt'
# kano.favourite='jai Hanuman'
# print(stavan.printdetail())

# class employee():
#     def __init__(self,asalary,arole,aname):
#         self.salary=asalary
#         self.role=arole
#         self.name=aname
#
#     def printdetail(self):
#         return f'salary is{self.salary} role of {self.role} name is {self.name}'
# stavan=employee
# kano=employee
# stavan.salary=100000
# stavan.role='student'
# kano.name='stavan'
# kano.salary=10000
# kano.role='hacker'
# kano.name='kano'
#
# print(stavan.salary)
#
# class programmar(employee):
#     def printprog(self):
#         return f'salary is{self.salary} role of {self.role} name is {self.name}'
# chetan=programmar(555,'bhai','chetan')
# karan=programmar(777,'boss','karan')
# print(karan.printdetail())


class employe:
    def __init__(self,asalary,arole,aname):
        salary=asalary
        role=arole
        name=aname
    def printdetail(self):
        return f'salary is{self.salary} and role is {self.role} and name is {self.name} '
stavan=employe
kano=employe
stavan.salary=100000
stavan.role='student'
stavan.name='stavan'

kano.salary=200000
kano.role='Bhole baba bhakt'
kano.name=kano

print(stavan.salary)

class programmar(employe):
    def prodetail(self):
        return f"salary{self.salary} role {self.role}name{self.name}"
anmol=programmar(111,'bhai','anmol')
chetan=programmar(222,'bhaiokabhai','chetan')
print(chetan.prodetail())












































