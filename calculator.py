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
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a,b):
    if a<=0 or b<=0 or a==1:
        return ValueError
    else:
        return math.log(b,a)

def exp(a,b):
    return a**b



def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b





def logarithm(a, b):
    if a<= 0 or b <= 0 or a == 1:
        raise ValueError
    else:
        return math.log(a, b)



def exponent(a, b):
    return a ** b
