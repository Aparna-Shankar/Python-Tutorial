
# Dictionary - key-value pairs

# Dictionaries are also not ordered and cannot have duplicates
# Does not support union, intersection & difference
# Cannot add or subtract dictionaries
# Dictionaries need not have the same keys. Keys can be either strings or numberss


# You can have a dictionary inside a list as shown below
players = [
    {
        'name': 'Rolf',
        'numbers': (2, 3, 6, 9)
    },
    {
        'name': 'Anne',
        'numbers': (3, 6, 4, 1)
    }
]


# To access the first element, use sbscript as it is a list
player_one = players[0]
print(player_one)

# To access the key value pairs of the dctionary, we use the keys
print(player_one['name'])
name_1 = player_one['name']
print(name_1)

# Aleternatively , we can also use the get()
print(player_one.get('name'))

# You can do operations on the dictionary key-value pairs
print(sum(player_one['numbers']))


student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

print(student)
# To print only the values in the dictionary
print(student.values())
# pop function is used to pop out a key-value pair from the dictionary.
age = student.pop('age')
print(age)
print(student.values())  # Prints the values without the age as it was popped out

print(student.get('name', 'Not Found'))
print(student.get('phone', 'Not Found'))

# To print all the values in the dictionay in a loop

for key, value in student.items():
    print(f'{key} : {value}')
