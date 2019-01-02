 ##Finding prime numbers for a user range using functions


##def get_prime (limit):
##    for n in range(2, limit):
##        for x in range(2, n):
##            if n % x == 0:
##                break
##        else: # Loop fell through without finding a factor
##            print(f'{n} is a Prime number!')
##
##
##user_limit = int(input('Enter the upper limit to find prime numbers :'))
##get_prime(user_limit)

##check if the number entered is prime


def check_if_prime(n):
    for x in range(2,n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number!')

number = int(input('Enter your number :'))
check_if_prime(number)
