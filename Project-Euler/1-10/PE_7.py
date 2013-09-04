#Problem 7 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
#that the 6th prime is 13.
#
#What is the 10001st prime number?
#
#This is a relatively simple question. It is also easily within the scope of a
#prime sieve solution.

import time
import os.path, sys
# An OS-independent hack for importing from the parent directory
sys.path.append(os.path.abspath(os.path.split(os.getcwd())[0]))
import pemaths

t = time.time()
myprimes = pemaths.Eratosthenes(200000)
print('The 100001st prime is {0}'.format(myprimes[10000]))
print('This took {0} seconds'.format(time.time() - t))