import sys

def fizzBuzz(n):
    if (1 <= n <= 100):
        if (n % 3 == 0 and n % 5 == 0):
            return 'FizzBuzz'  
        elif (n % 3 == 0):
            return 'Fizz'
        elif (n % 5 == 0):
            return 'Buzz'
        else:
            return n
    else:
        return None