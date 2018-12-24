
# Comparisons
# Equal			:	==
# Not Equal		:	!=
# Greater		:	>
# Less			:	<
# GE			:	>=
# LE			:	<=
# Obj Identity	:	is ( to check if they have the same object in memory)

# Python doesn't have switch case 


language = 'Java'

if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
elif language == '.Net':
	print('Language is .Net')
else:
	print('No Match')


# and
# or
# not (switches a Boolean)

user = 'Developer'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')
elif not logged_in:
	print('Please Log in')
else:
	print('Bad Creds')


# Object Identity

a= [1,2,3]
b= [1,2,3]
print(a==b)
print(a is b) # returns False as there sre 2 different objs in memory

b= a

print(id(a)) 
print(id(b))

print(a is b)


# False Values in Python:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


#condition = None
#condition = 0
#condition = {} #enpty dictionary

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') 
