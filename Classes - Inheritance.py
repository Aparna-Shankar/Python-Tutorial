
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


class Developer(Employee):  # Developer class inherits from Employee
    raise_amount = 1.01

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Employee class's init method will handle first, last & pay
        self.prog_lang = prog_lang


class Manager(Employee):  # Manager class inherits from Employee
    raise_amount = 1.09

    def __init__(self, first, last, pay, employees=None):  # never plan mutable lists as arguments
        super().__init__(first, last, pay)  # Employee class's init method will handle first, last & pay
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """Adds an employee from the list """
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """Removes an employee from the list"""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """Print employees from the list"""
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Aparna', 'Shankar', 60000, 'Python')
dev_2 = Employee('Abhi', 'Pednekar', 60000)

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# dev_2.apply_raise()
# print(dev_2.pay)  # Developer and Employee raises are different just by declaring their instances with different classes


dev_1 = Developer('Aparna', 'Shankar', 60000, 'Python')
dev_2 = Developer('Abhi', 'Pednekar', 60000, 'Java')

mgr_1 = Manager('Sreeja', 'PK', 90000, [dev_1])


# print(dev_1.email)
# # mgr_1.prog_lang # This will throw an error as manager doesn't inherit from Developer but only from Employee
# print(dev_2.prog_lang)
# print(mgr_1.email)


mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
#
print(isinstance(mgr_1, Developer)) # for instances
print(issubclass(Manager, Employee)) # for classes
