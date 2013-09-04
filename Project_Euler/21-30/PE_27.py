#Problem 27 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Euler published the remarkable quadratic formula:
#
#n^(2) + n + 41
#
#It turns out that the formula will produce 40 primes for the consecutive values
#n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
#by 41, and certainly when n = 41, 41^(2) + 41 + 41 is clearly divisible by 41.
#
#Using computers, the incredible formula  n^(2) - 79n + 1601 was discovered,
#which produces 80 primes for the consecutive values n = 0 to 79. The product of
#the coefficients, 79 and 1601, is 126479.
#
#Considering quadratics of the form:
#
#n^(2) + an + b, where |a| < 1000 and |b| < 1000
#
#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |-4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression
#that produces the maximum number of primes for consecutive values of n,
#starting with n = 0.
###
#There are two million possible unique combinations to consider. Double positive
#or double negative are the same, as well as alternating sign for either a or b.
#Each combination would be used to generate values for incremental n, until a
#yielded value was not prime (I think the best way to do this is check against
#a list of known primes). This build and check method is where the major costs
#will occur. I sped the process up by restricting b to prime values and a to odd
#ones: explained below.

import time
import os.path, sys
# An OS-independent hack for importing from the parent directory
sys.path.append(os.path.abspath(os.path.split(os.getcwd())[0]))
import pemaths

def qForm(n, a, b):
    '''Using the input values, returns the value of the quadratic formula.'''
    return((n ** 2) + (a * n) + b)

def checkPrime(val, primes):
    '''A special function to check if a given value exists in a list of primes.
    This optimization is possible thanks to the list being numerically sorted by
    value.'''
    for p in primes:
        if val == p:
            return True
        elif val < p:
            return False
    raise ValueError('Primes list was too short! Test value exceeded highest \
prime value.')

t = time.time()  # Start the timer
CONST = 1000
#The largest potential prime is determined by the highest n, a, and b
#values of b and a are constrained, n is unknown, so we guess an upper limit and
#checkPrime() will let us know if it is too small. The function is also written
#to remove the penalty of this value being too large.
primes = pemaths.Eratosthenes(20000)
#b must be prime, a requirement of the case n = 0
bvals = pemaths.Eratosthenes(CONST)

a = (CONST - 1) * (-1)
max_n = 0
max_a_b = (0, 0)
while a < CONST:
    for b in bvals:
        n = 0
        while checkPrime(qForm(n, a, b), primes):
            n += 1
        if n > max_n:
            max_n = n
            max_a_b = a, b
    #a must be odd: consider the quadratic formula as n(n + a) + b = Prime(odd)
    #if a were even, then for every odd n, the test value would be even
    a += 2
solution = max_a_b[0] * max_a_b[1]
t = time.time() - t
print('A = {0}, B = {1}: {2} primes'.format(max_a_b[0], max_a_b[1], max_n))
print('A * B = {0}'.format(solution))
print('This took {0} seconds'.format(t))
    



