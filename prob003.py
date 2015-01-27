"""
Project Euler -----
Problem Number: 003
-----------------------------------------------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Mario Garcia
"""

# import matefuncs as mf

def getPrimeFactors(x):
    """
    This function takes a number and returns its factors in a list
    """
    a = []
    b = []
    for i in xrange(1, x + 1):
        if x % i == 0:
            a.append(i)
            
    return a

# Get a list of all Fibonacci numbers up to n = 4 000 000
n = 13195

a = getPrimeFactors(n)
print a



# b = []
# for i in a:
# 	if mf.is_prime(i):
# 		b.append(i)

# print b
# print sum(b)