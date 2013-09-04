#A library of utility methods that can be used in multiple problems presented
#by Project Euler.
#By Paul Barton

import math
import time

def Eratosthenes(n):
    """
    A Sieve of Eratosthenes method for the rapid computation of primes less
    than or equal to the provided integer n. Coerces to integer. Returns a list
    comprised of primes.
    """
    n = int(n)
    candidates = range(n+1)
    fin = int(n**0.5)
    #Loop over the candidates, marking out each multiple.
    #If the current candidate is already checked off then
    #continue to the next iteration.
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n/i - 1)  # This is an obscure python
        #list expression that returns a list [from 2*i by multiples of i to end]
    #Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

def primeFactorize(n, powers=True, primes=False):
    """
    A function that computes the prime factors of a given integer n. The
    optional "powers" argument provides the ability to return a 2D list pairing
    primes with their respective powers (True), or a 1D list representing only
    the primes (False). The function will accept a pre-generated list of primes
    as the optional "primes" argument (use-case: repetitive calls), otherwise it
    will call Eratosthenes itself to generate them.
    """
    n = int(n)
    if not primes:
        primes = Eratosthenes(n)
    pfacts = []
    if n in [0,1]:
        print('0 and 1 have no prime factors')
        return []
    else:
        while n != 1:
            for p in primes:
                d, r = n / p, n % p
                c = 0
                while not r:
                    c += 1
                    n = d
                    d, r = n / p, n % p
                if c:
                    pfacts.append([p, c])
        if powers:
            return pfacts
        else:
            newlist = []
            for i in pfacts:
                newlist.append(i[0])
            return newlist

def factorial(n):
    """
    This function computes the value of n factorial, provided an integer n.
    This works well for n <= 997 on my machine due to recursion limits. If more
    is needed, math.factorial may be used (for repeated operations, it *should*
    be used as it is twice as fast). This function will attempt to coerce its
    input to an integer.
    """
    n = int(n)
    return _factorial(n)
    
def _factorial(n):
    """The recursive core of the factorial function"""
    if n in [0,1]:
        return 1
    else:
        c = _factorial(n - 1)
    return (c * n)
