# Python Object Oriented Programming

# A Class will have attributes and methods
# A class is defines so that the data and it's associated actions(functions) can be combined into a single entity
# This cannot be done in a dictionary


class Employee:
    def __init__(self, first, last, pay):  # Here self is the instance variable. It is blank object that gets created before the
        self.first = first                 # __init_(dunder) function is created. It gets it's first value when we assign 'first'
        self.last = last
        self.pay = pay
        self.email = f'{first}_{last}@company.com'

    def fullname(self):
        # return f'{self.first} {self.last}'
        return '{}{}'.format(self.first, self.last)



# Instance variables/Objects
empl_1 = Employee('Aparna', 'Shankar', 60000)
empl_2 = Employee('Abhi', 'Pednekar', 60000)


print(empl_1.email)
print(empl_2.email)

# 2 ways of accessing the methods
print(empl_1.fullname())
print(Employee.fullname(empl_1)) # here we need to pass the instance as the argument

