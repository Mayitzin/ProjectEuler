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


def getFactors(x):
    """
    This function takes a number and returns its factors in a list
    """
    a = []
    for i in xrange(1, x + 1):
        if x % i == 0:
            a.append(i)
    return a


def is_prime(x):
    import numpy as np
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = np.sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

# num = 23 # try num = 1011013, num = 10110133, num = 101101331
# if is_prime(num):
#     print str(num) + " is a prime number"
# else:
#     print str(num) + " is a composite number"