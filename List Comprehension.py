# List comprehension is a Pythonic way of constructing a List

numbers = list(range(10))
print(numbers)

# double = []
# for n in numbers:
#     double.append(n * 2)
# print(double)

# The above can be achieved by list comprehension as shown below:
double = [n * 2 for n in numbers]
print(double)

##phrases = [f'I have {num} apples' for num in double]
##print(phrases)
##
##
##roomies = ['Ann', 'Nisha', 'Rony', 'Nithya', 'Lesitha']
##lc_roomies = [name.lower() for name in roomies]
##print(lc_roomies)
##
####To check if an entered value is part of the string
##chk_roomie = input("Enter your friend's name : ")
##if chk_roomie in roomies:
##    print(f'{chk_roomie} was your roomie!')
##else:
##    print(f'{chk_roomie} was not your roomie.')


##List Comprehensions with Conditionals

evens = [n for n in numbers if n % 2 == 0]
print(evens)

friends = ['ann', 'jasu', 'abhi', 'nisha']
guests = ['Ann', 'Nisha', 'Rony', 'Nithya', 'Lesitha']

friends_in_guests = [name for name in guests if name.lower() in friends]

##OR
friends_in_guests = [name.capitalize() for name in friends if name.capitalize() in guests]
print(friends_in_guests)
