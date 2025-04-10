"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        if math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(b, a):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a


def logarithm(a, b):
    if a<= 0 or b <= 0 or a == 1:
        raise ValueError
    else:
        return math.log(a, b)



def exponent(a, b):
    return a ** b

