##Finding a prime number in a Range

##for n in range(2,10): # [2,3,4,5,6,7,8,9] range is from 2 to 10 not including 10
##    for x in range(2,n): #[],[2],[2,3],[2,3,4],[2,3,4,5] etc
##        if n % x  == 0:
##            print(f'{n} equals {x} * {n//x}')
##            break
##    else: # This else is the ELSE of the FOR loop. It gets executed when the FOR loop
##            # finishes executing completely. The ELSE will NOT run if the for loop encounters a BREAK
##        print(f'{n} is a Prime Number')
        


##for x in range (2,50):
##    for n in range(2,x):
##        if x % n == 0:
####            print(f'{x} is not a Prime Number')
##            break
##    else:
##        print(f'{x} is a Prime Number!')


##Print out 100 numbers from 1 to 100 both inclusive, but:
##Instead of printing multiples of 3, print Fizz
##Instead of printing multiples of 5, print Buzz
##Instead of printing multiples of both 3 and 5, print FizzBuzz

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
        
