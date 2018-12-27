# Data structures - Collections


# Lists - Mutable  Ordered
print('____________________ LISTS ________________________')
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_1[0])  # subscript can be accessed via indexing
print(list_2)

# Mutable
list_1[0] = 'Art'
list_1.append('History')
#list_1.add('English')  List object does not have the 'add' attribute
print(list_1)
print(list_2)


# Tuples - Immutable - Ordered
print('____________________ TUPLES ________________________')
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
# tuple_3 = ('English') #Note that this is NOT a tuple. Python identifies a tuple by the comma
tuple_3 = ('English',)  # This is a tuple. In fact, tuple_2 = 'History', is also a tuple

print(tuple_1)
print(tuple_1[0])  # subscript can be accessed via indexing
print(tuple_2)

# Non Mutable
# tuple_1[0] = 'Art' # Does not support assignment
# tuple_1.append('Art') # Does not support append

# However the below is supported

tuple_1 = tuple_1 + tuple_3
print(tuple_1)

# Sets - unordered - cannot rely on them to be ordered
print('_____________________ SETS ________________________')
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
# print(cs_courses[0]) Sets do not support indexing as the values are not fixed
# cs_courses.append('English') # Not supported

# However you can add to a set variable as shown below
cs_courses.add('English')
print(cs_courses)
# Now they also remove duplicates. So if you try to add the same element again:
cs_courses.add('English')
print(cs_courses

      )
