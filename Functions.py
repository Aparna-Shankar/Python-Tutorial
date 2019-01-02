
# def hello_func(greeting, name='Abhi'):
#     # pass  # to tell that we dont want to do anything in the function

#     # return '{}, {} Function!'.format(greeting, name)
#     # **** OR ******
#     return f'{greeting}, {name} Function!'


# # for x in range(2):
# #     print (hello_func().upper())
# # # print (hello_func('Hello'))


# print(hello_func('Hi', 'Appu'))

#-----------------------------------------------------------------------------------------------------

# *args & **kw(keyword) args are used when we don't know how many arguments are passed

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# # student_info('Math', 'Art', name='John', age=22)


# courses = ['Math', 'Art']  # List
# info = {'name': 'John', 'age': 22}  # Dicttionary
# student_info(*courses, **info)  # If the asterisks are not used, the values are not unpacked

#-----------------------------------------------------------------------------------------------------


# # Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""  # doc string for explaining what the function does

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]


# print(is_leap(2016))
# print(days_in_month(2016, 2))


#-----------------------------------------------------------------------------------------------------

# Lambda functions - Annonymous function or funcions with no name

# def add_two(x, y):
#     return x + y

# The above can be written as a lamda function. But since there is no name defined, lamda functions
# cannot be defined and left as is as they die immediately.
# #lambda x,y: x+y -- This cannot be used anywhere

# so it is defined more like this:
# add = lambda x,y : x+y

# print(add(4, 5))


#-----------------------------------------------------------------------------------------------------

# First Class functions - are functions that you can pass as an argument to another fucntion
# Higher Order functions - are functions that accept another fucntion as the parameter

def who(data, identify):  # who is the Higher order function and identify is the first class function
    return identify(data)  # Here's where we are executing the indentifier function


# def my_identifier(some_data):
#     return some_data['name']


user = {'name': 'Aparna', 'surname': 'Shankar', 'adhar': '23934390'}
# print(who(user, my_identifier))  # Here we are not executing the function, we are just referring to it.

# The identifier function can be re-written as a lambda function. So Lambda functions are extremely useful when they are used as a first class fucntion
print(who(user, lambda id: id['adhar']))
print(who(user, lambda id: id['name']))

#-----------------------------------------------------------------------------------------------------
