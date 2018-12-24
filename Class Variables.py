# Class Variables are shared among all instances of a class
# Instance vriables can be unique for each instance


class Employee:

    num_of_emp = 0 # This class variable is to maintain the total employee count
    raise_amount = 1.04  # Class Variable

    def __init__(self, first, last, pay):  # Here self is the instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}_{last}@company.com'
        Employee.num_of_emp += 1 # here we don't need to access it at an instance level because each employee instance will not have a separate employee count

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instance variables
empl_1 = Employee('Aparna', 'Shankar', 60000)
empl_2 = Employee('Abhi', 'Pednekar', 60000)




# print(empl_1.email)
# print(empl_2.email)

# 2 ways of accessing the methods
# print(empl_1.fullname())
# print(Employee.fullname(empl_1))  # here we need to pass the instance as the argument

# Calling the method
# empl_1.apply_raise()
# print(empl_1.pay)

# print(Employee.raise_amount) # accessing the class variable from class
# print(empl_1.raise_amount)   # accessing the class variable from instance
# print(empl_2.raise_amount)

# #  To print the name space of the class
# print(Employee.__dict__)

# #  To print the name space of the instance
# print(empl_1.__dict__)

Employee.raise_amount = 1.05  # This changes the class variable on the entire class
empl_1.raise_amount = 1.04 # This adds the class variable to the namespace of the instance
print(empl_1.__dict__)

print(Employee.raise_amount)  # accessing the class variable from class
print(empl_1.raise_amount)   # accessing the class variable from instance
print(empl_2.raise_amount)
