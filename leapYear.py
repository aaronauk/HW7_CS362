import sys

def leapYear(y):
    if (y % 4 != 0):
        return False
    if (y % 100 != 0):
        return True
    if (y % 400 == 0):
        return True