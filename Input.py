
# Accepting input from the screen
my_name = 'Aparna'
your_name = input('Enter your name: ')
print(f'Hello, {your_name}')


num1 = input('Enter first number:  ')
num2 = input('Enter second number: 	')
print('Numbers entered are: ', num1,num2)
print(eval(num1) +eval( num2))


# your_age = input('Please enter your age: ')

# print(f'You have lived for {your_age * 12} months.')   #This would just concatenate the age 12 times. Anything that is fed into the input function is a string

# Typecast
age_num = int(your_age)
print(f'You have lived for {age_num * 12} months')

# Better way of writing it
your_age = int(input('Please enter your age :  '))
print(f'You have lived for {age_num * 12} months')

# Calculate the age in seconds
age_in_sec = your_age * 365 * 24 * 60 * 60
print(f'You have lived for {age_in_sec} seconds!')

