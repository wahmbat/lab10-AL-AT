"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example

def add(a, b): 
    return a + b

def substract(a, b):
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
        return math.log(a, b)
    else:
        raise ValueError


def exponent(a, b):
    return a ** b
