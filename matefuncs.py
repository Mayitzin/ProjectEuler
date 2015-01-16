"""
This module has the most common mathematical functions that may appear
in the problems of Project Euler. See:
https://projecteuler.net/

@author: Mario Garcia
"""

def fib(n, enlist=False):
    """
    This function returns the nth number in the Fibonacci series. The
    series starts with zero as:
    1, 1, 2, 3, 5, 8, etc...
    """
    if enlist is True:
        l = []
    # Initial values
    a, b = 0, 1
    #Start Looping
    for i in range(n):
        a, b = b, a + b
        if enlist is True:
            l.append(a)
    # Return values
    if enlist is True:
        return l
    else:
        return a


def fiblim(m, enlist=False):
    """
    This function returns the first n values in the Fibonacci series,
    which not exceed the value of m. The series starts with one as:
    1, 1, 2, 3, 5, 8, etc...
    """
    if enlist is True:
        l = []
    # Initial values
    a, b = 0, 1
    #Start Looping
    for i in range(1000):
        if a < m:
            a, b = b, a + b
            if enlist is True and a<m:
                l.append(a)
        else:
            break
    # Return values
    if enlist is True:
        return l
    else:
        return b-a