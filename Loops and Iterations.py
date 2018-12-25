
# For Loop

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        # break  (break out of the loop)
        continue   # continue with next iteration of the loop
    print(num)

# Nested loops
# nums = [1,2,3,4,5]
# for num in nums:
#   for letter in 'abc':
#       print(num, letter)


# Range
for i in range(10):
  print(i)

# While Loops
# Ctrl + C - To break out of an infinite loop
# x = 0
# while True:
#     if x == 4:
#         break
#     print(x)
#     x+= 1
