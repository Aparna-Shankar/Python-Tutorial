

class Employee:

    # Double underscore methods are called Dunder methods
    def __init__(self, first, last, pay):  # Here self is the instance variable
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # Property decorator allows us to access a method just like we access an attribute. If the email method was not defined with a property decorator, we would have to get the email by calling it as a method.
    @property
    def email(self):
        return f'{self.first}_{self.last}@company.com'

    # Setter decorator
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # deleter decorator
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


empl_1 = Employee('Aparna', 'Shankar', 60000)
empl_2 = Employee('Abhi', 'Pednekar', 60000)


empl_1.first = 'Chinju'

print(empl_1.first)
# With @property
print(empl_1.email)
# Without @property
# print(empl_1.email()
print(empl_1.fullname)

empl_1.fullname = 'Aparna Shankar'  # Can't do this without a setter
print(empl_1.first)


del empl_1.fullname
print(empl_1.first)
