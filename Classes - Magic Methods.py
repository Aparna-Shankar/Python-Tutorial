

class Employee:

    num_of_emp = 0  # This class variable is to maintain the total employee count
    raise_amount = 1.04  # Class Variable

    # Double underscore methods are called Dunder methods
    def __init__(self, first, last, pay):  # Here self is the instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}_{last}@company.com'

        """ Here we don't need to access it at an instance level 
        because each employee instance will not have a separate employee count"""
        Employee.num_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """Representation of the object - Can be used in logs etc. To look at the object & understand what it is"""
    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    """Usually represents the values in the object. Str method takes precedence over repr"""

    def __str__(self):
        return f'Employee Details : {self.fullname()} - {self.pay}'

    """It is the best practice to have a repr & str methods for every class that you code"""
    def __add__(self, other):
        """ Dunder method redefines add function to return the sum of salaries of the 2 employees passed """
        return self.pay + other.pay
                    # OR by using the dunder add method
        # return int.__add__(self.pay, other.pay)

    def __len__(self):
        """ Dunder method redefines len function to return the length of full name of the employee """
        return len(self.fullname())


empl_1 = Employee('Aparna', 'Shankar', 60000)
empl_2 = Employee('Abhishek', 'Pednekar', 60000)

# print(empl_1)
# print(repr(empl_1))
# print(str(empl_1))

# print(int.__add__(1,2))
# print(str.__add__('Abhi', 'Aparna'))
#
# print(empl_1 + empl_2)


print(len('test'))
print('test'.__len__())

# print(len(empl_1))
