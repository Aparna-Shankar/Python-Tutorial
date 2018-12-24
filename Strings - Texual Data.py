print('Hello World')

greeting = 'Hello'
name = 'Abhi'

message = greeting + name

print(message)

#Length
print(len(message))
#Indexes
print(message[4])
print(message[:5])
print(message[6:])

#Other Functions
print(message.lower())
print(message.upper())
print(message.count('l')) #To get the number of occurrences of the argument
print(message.find('l')) #To find the position of the argument
print(message.replace('Abhi', 'Aparna'))

#Concatenation
message = '{}, {}. Welcome!'.format(greeting, name)

#Using F strings
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)


# To see all available attributes and methods that we have access to
print(dir(message))
print(help(str))
print(help(name.lower))

# print(help(str.count))