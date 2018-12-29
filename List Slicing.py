#  List slicing is mainly used to slice off from a list or create a new list

friends = ['Ann', 'Jasu', 'Abhi', 'Teena', 'Jacob']

# forward index
# ['Ann', 'Jasu', 'Abhi', 'Teena', 'Jacob']
#     0       1       2       3       4
# Reverse index
# ['Ann', 'Jasu', 'Abhi', 'Teena', 'Jacob']
#   -5      -4      -3       -2       -1


print(friends[2:4])  # This is similar to range. Prints everything from 2 to 4 not including 4

print(friends[2:])
print(friends[:2])

# To return the last element of a list
print(friends[-1])

# To reverse traverse a list
print(friends[-3:-1])
print(friends[:-3])
