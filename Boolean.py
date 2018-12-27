age = 20
#Comparison operators
is_over_age = age >= 18
is_under_age = age <=18
is_twenty = age == 20
my_num = 5
user_num = int(input('Enter your number: '))
print(my_num == user_num)

#AND/ OR/ NOT

yes = True and True
no  = True and False

print(no)

#OR in Python works by fetching the 2nd value ONLY if the first one is false.
#If the 1st one is TRUE, it never evaluates the 2nd and returns a TRUE

first_one = True or False
second_one = False or True
always_true =  True or True
neither = False or False

# NO - Invert operator
absolutely = not False #True
never      = not True # False


is_programmer = True
is_learning   = False
is_awesome    = is_programmer and is_learning
less_awesome  = is_programmer and not is_learning

is_designer   = False
great_guys    = ((is_programmer or is_designer) and (not is_learning))
               #either programmer, designger and learning
print(great_guys)



