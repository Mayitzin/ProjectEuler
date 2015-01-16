"""
Project Euler -----
Problem Number: 001
-----------------------------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: Mario Garcia
"""

import numpy as np

# Select and sum the even numbers of the list
s = 0
for i in range(1000):
	if (int(np.mod(i,3)) is 0) or (int(np.mod(i,5)) is 0):
		s += i

# Print the sum
print s