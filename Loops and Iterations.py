
# For Loop

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        # break  (break out of the loop)
        continue   # continue with next iteration of the loop
    print(num)

kid_ages = (2, 5)
for age in kid_ages:
    print(f'I have a {age} year old kid')

# in both the examples above, the list and the tuples are sequences and the for loop knows that it should stop the execution at the end of the sequence. Lists and tuples are ITERABLES


cars = ['ok', 'ok', 'ok', 'ok', 'faulty', 'ok']
for car_status in cars:
    if car_status == 'faulty':
        print(f'Stop the production line')
        break
    print(f'This car is {car_status}')

for num in range(2, 10):
    if num % 2 == 0:
        print(f'Found an even number, {num}')
        continue
    print(f'Found a number, {num}')

# Nested loops
# nums = [1,2,3,4,5]
# for num in nums:
#   for letter in 'abc':
#       print(num, letter)


# Range
# for i in range(10): # Range function is called a generator in Python. Range function lists down the numbers from 0 to 9. The Range function is also an ITERABLE
#   print(i)


# A Dictionary is also an ITERABLE and can be ised with a FOR loop

my_friends = {
    'Abhi': 0,
    'Ann': 200,
    'Jasu': 120
}

# for name in my_friends:
#     print(f'I last saw {name} {my_friends[name]} days ago')

#       OR there is an easier way in python 3
for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago')

# print(my_friends.items()) # [('Abhi', 0), ('Ann', 200), ('Jasu', 120)]

# Understanding items or de-structuring a tuple

# for t in [('Abhi', 0), ('Ann', 200), ('Jasu', 120)]:
#     n, v = t  # or (n,v) = t
#     print(n)
#     print(v)

#     # OR

# for n, v in [('Abhi', 0), ('Ann', 200), ('Jasu', 120)]:
#     print(n)
#     print(v)


# While Loops
# Ctrl + C - To break out of an infinite loop
# x = 0
# while True:
#     if x == 4:
#         break
#     print(x)
#     x += 1
