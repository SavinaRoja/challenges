#Problem 10 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#
#Though I considered updating this solution to simply call my more recent prime
#sieve, but I thought I would leave it for illustration and posterity. I made
#this prime sieve function before even knowing the term. It's a slow
#implementation of the Eratosthenes sieve, but it works.

from time import time

s = time()

LIMIT = 2000000
NATURALS = range(LIMIT)
PRIMES = []

index = 2
while index < len(NATURALS):
    if NATURALS[index]:
        current = NATURALS[index]
        NATURALS[index] = 0
        PRIMES.append(current)
        n = 1
        while (n * current) < LIMIT:
            try:
                NATURALS[n * current] = 0
            except IndexError:
                pass
            n += 1
        index += 1
    
    else:
        index += 1
print('sum: {0}'.format(sum(PRIMES)))
f = time()
print('time: {0}'.format(f-s))

### If you'd like to compare this to the newer sieve, uncomment the following:

#import os, os.path, sys
#sys.path.append(os.path.abspath(os.path.split(os.getcwd())[0]))
#import pemaths

#print('New Eratosthenes\' Sieve:')
#s = time()
#print('sum: {0}'.format(sum(pemaths.Eratosthenes(LIMIT))))
#print('time: {0}'.format(time() - s))

