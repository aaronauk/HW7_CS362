import sys

def fizzBuzz(n):
    if (n % 3 == 0 and n % 5 == 0):
        return 'FizzBuzz'  
    elif (n % 3 == 0):
        return 'Fizz'