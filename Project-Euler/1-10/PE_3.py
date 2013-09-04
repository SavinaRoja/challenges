#Problem 3 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#
#This problem requires one to find the prime factors of a number and return the
#largest of them. Efficiency for finding primes can vary hugely, I present here
#two ways of going about this with a comparison of time. The first is my early
#code, and the second is an implementation of the Sieve of Eratosthenes.

import time

NUMBER = 600851475143

def isprime(inniger):
    '''A method for testing primality, It scans all integers from 2 to n/2 for
    n and returns False if it finds a divisor. This is a very inefficient
    method'''
    j = 2
    while (j < (inniger/2 + 1)):
        test = inniger % j
        if test == 0:
            return False
        else:
            j+=1
    return True
    
prime_factors = []
thing = 2

t = time.time()
#I start with 2 as a first prime. I increase this by oneand every time I have
#found a prime, I see if it divides into the NUMBER. When a divisor is found,
#NUMBER is altered to the result of the division operation.
while not isprime(NUMBER):
    if isprime(thing) == True:
        test = NUMBER % thing
        if test == 0:
            prime_factors.append(thing)
            NUMBER = NUMBER/thing
            thing = 2
        else:
            thing += 1
    else:
        thing += 1
prime_factors.append(NUMBER)
print(prime_factors[-1])
print('Very naive method took {0} seconds'.format(time.time() - t))

#Here is a more efficient solution using The Sieve of Eratosthenes
def Eratosthenes(n):
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
t = time.time()  
primes = Eratosthenes(NUMBER)
for p in reversed(primes):
    if not NUMBER % p:
	print(p)
	break
print('Eratosthenes Sieve method took {0} seconds'.format(time.time() - t))

