# try:
# 	pass
# except Exception:
# 	pass

"""Types of built-in errors
-> IndexError - when we try to access an index that does not exist
-> NameError - when variables are not defined
-> KeyError - when we specify an incorrect key value in a dictionary or try accessing a list using a key value
-> AttributeError - related to objects. eg: List object has no attribute 'intersection'
					because intersection can be used only with sets
-> NotImplementedError - can be used in methods that are not yet implemented
-> RuntimeError - it's a base class. mostly other errors inherit from it. So RTE occurs rarely
-> SyntaxError - when we make mistakes in the Python Syntax
-> IndentationError - when we do not provide sufficient indentation after functions, classes etc
-> TabError - happens while switching between editors (ie using tabs and spaces)
-> TypeError - when performing operations on incompatible data types
-> ValueError
-> ImportError - circular imports
-> DeprecationWarning ->

"""

class Car:
	def __init__(self, make, model):
		self.make = make
		self.model = model

class Garage:
	def __init__(self):
		self.cars = []

	def __len__(self):
		return len(self.cars)

	def __getitem__(self, item):
		return self.cars[item]

# """ Raising a NotImplemented Error"""
# 	def add_car(self, car):
#     raise NotImplementedError("We can't add cars to the garage yet")

	def add_car(self, car):
		if not isinstance(car, Car): #Validation is done within the function itself and not BEFORE calling the function
			raise TypeError(f"Tried to add a {car.__class__.__name__} to garage, but you can only add 'Car' object")
		self.cars.append(car)

	def __repr__(self):
		return f'Garage has {len(self.cars)} cars'


honda = Garage()

try:
	honda.add_car( 'City' ) # This would raise the type error
	# honda.add_car(Car('Honda', 'City'))
	# honda.add_car(Car('Honda', 'Jazz'))

except TypeError:
	print('Your car was not a CAR!')

except ValueError:
	print('User error!')

finally: #this block executes all the time - whether or not the error happened
	print(honda)

# for i in range(len(honda)):
# 	print(honda.cars[i].model)

