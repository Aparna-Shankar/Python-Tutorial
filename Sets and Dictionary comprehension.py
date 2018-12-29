# Sets and Dictionary comprehension
# Sets comprehension - it is exactly the same as list comprehension

friends = {'ann', 'jasu', 'abhi', 'nisha'}
guests = {'ann', 'nisha', 'rony', 'nithya', 'lesitha'}

# guests_in_friends = {name for name in guests if name.lower() in friends}


# However there is an even better way of doing this in sets using the intersection operator. Remember that the operators are case  sensitive
guests_in_friends = {name.capitalize() for name in friends & guests}
print(guests_in_friends)

# Dictionary comprehension
names = ['Ann', 'Nisha', 'Rony', 'Nithya', 'Lesitha']
time_last_seen = [90, 365, 200, 456, 765]

friends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}


# This can also be done in the following manner
# print(zip(names, time_last_seen))  # Returns a zip object whose .__next__() returns a tuple [(Ann,90),(Nisha,365), (Rony,200)...]
# Then we call a dict() on the above, we get a Dictionary (turns them into a key-value pair)

friends_last_seen = dict(zip(names, time_last_seen))
print(friends_last_seen)
