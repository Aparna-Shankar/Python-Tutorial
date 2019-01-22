# Regular methods automatically takes the instance as the 1st parameter
# Class methods takes the class as the 1st parameter


class Employee:

    num_of_emp = 0  # This class variable is to maintain the total employee count
    raise_amount = 1.04  # Class Variable

    def __init__(self, first, last, pay):  # Here self is the instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}_{last}@company.com'
        Employee.num_of_emp += 1  # here we don't need to access it at an instance level because each employee instance will not have a separate employee count

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """Class methods are used whenever we want alter values of class variables. Class Methods 
    allow the inherited classes to use them"""
    @classmethod  # decorator - alters the functionality of the method
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    """Another area where class methods are used - when we want to create an instance from
    a float, int , string etc"""
    @classmethod  # Alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # This will call the init method and is equivalent to calling the init method via Employee( first, last, pay)


# Static Methods - They accept neither class nor instance as parameter
    @staticmethod
    """Static methods are like class methods but does not provide the generic form of 
    returning a class type. it is more specific. 
    Static methods are used when we know that the class we are writing will not be inherited from
    """
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Instance variables
empl_1 = Employee('Aparna', 'Shankar', 60000)
empl_2 = Employee('Abhi', 'Pednekar', 60000)

Employee.set_raise_amt(1.16)

# # This is equivalent to
# # Employee.raise_amount = 1.16


print(Employee.raise_amount)  # accessing the class variable from class
print(empl_1.raise_amount)   # accessing the class variable from instance
print(empl_2.raise_amount)

empl_1.set_raise_amt(1.06)

print(Employee.raise_amount)
print(empl_1.raise_amount)
print(empl_2.raise_amount)


# empl_str_1 = 'Ann-Mary-60000'
# empl_str_2 = 'Renjith-Thomas-60000'

# empl_3 = Employee.from_string(empl_str_1)
# empl_4 = Employee.from_string(empl_str_2)



#******************************************************************************************************
# Static Methods - They don't pass anything automatically -neither class nor instance


# import datetime
# my_date = datetime.date(2018, 10, 6)
# print(Employee.is_workday(my_date))
#
# # print(empl_3.first)