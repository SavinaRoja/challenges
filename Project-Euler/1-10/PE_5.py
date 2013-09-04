#Problem 5 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#2520 is the smallest number that can be divided by each of the numbers from 1
#to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

import time
import os.path, sys
# An OS-independent hack for importing from the parent directory
sys.path.append(os.path.abspath(os.path.split(os.getcwd())[0]))
import pemaths

#Here is some naive brute force code. It's cleaned up from an old version.
#Take a look at the version history for the differences.
def oldBrute(interval=20):
    t = time.time()
    factors = range(interval / 2, interval)
    test = interval
    c = False
    while not c:
        c = True
        for i in factors:
            if test % i:
                c = False
                break
        if c:
            print(test)
            break
        else:
            test += interval
    print('The old brute force method took {0} seconds'.format(time.time() - t))

#This is just a means of conducting the timing for the recursive brute force
#function. See new_brute() for the actual algorithm.
def newBrute(interval):
    t = time.time()
    print(new_brute(interval))
    print('The new brute force method took {0} seconds'.format(time.time() - t))
    
#Here is a recursive brute force solution that is extremely fast. It is
#limited by recursion depth however, so I made an iterative version as well.
#The basic concept is that the (i)th solution is some multiple of the (i-1)th
#solution.
def new_brute(interval):
    if interval:
        c = new_brute(interval - 1)
    else:
        return 1
    n = c
    while c % interval:
        c += n
    return c
    
#Here is an iterative version of the solution illustrated in new_brute()
def iterBrute(interval):
    t = time.time()
    ci = 2
    val = 2
    while ci < (interval + 1):
        inc = val
        while val % ci:
            val += inc
        ci += 1
    print(val)
    print('The iterative brute force method took {} seconds'.format(time.time() - t))
    
#And here is the "elegant" solution which uses prime factorization to find LCMs
#I will need to look at it to see if it can be further optimized.
#This runs slower for small n, but scales well and runs faster for large n
def elegant(interval):
    t = time.time()
    primes = pemaths.Eratosthenes(interval)
    powers = [0] * (interval + 1)
    for i in range(2, interval + 1):
        pfacts = pemaths.primeFactorize(i, primes)
        for prime, power in pfacts:
            if power > powers[prime]:
                powers[prime] = power
    value = 1
    for v in range(interval + 1):
        if powers[v]:
            value = value * (v ** powers[v])
    print(value)
    print('The elegant method took {0} seconds'.format(time.time() - t))

def main():
    '''Main script. Modify which scripts are run for comparison by commenting lines'''
    
    TEST = 20  # Interval: At large values recursion may fail, comment it out
    
    #oldBrute(TEST)  # Old brute force: more naive (MUCH slower)
    
    newBrute(TEST)  # New brute force: less naive, recursive
    
    iterBrute(TEST)  # New brute force: less naive, iterative
    
    elegant(TEST)  # Elegant solution using prime factorization to find LCMs
    
if __name__ == '__main__':
    main()