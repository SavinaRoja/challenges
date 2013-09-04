#Problem 26 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#A unit fraction contains 1 in the numerator. The decimal representation of the
#unit fractions with denominators 2 to 10 are given:

#1/2 =   0.5
#1/3 =   0.(3)
#1/4 =   0.25
#1/5 =   0.2
#1/6 =   0.1(6)
#1/7 =   0.(142857)
#1/8 =   0.125
#1/9 =   0.(1)
#1/10 =  0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
#seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
#its decimal fraction part.
#
#Though primes appear to consistently produce recurring cycles, non-primes also
#produce such expansions.
#Below I implemented a moderately fast brute force method from two different
#starting points, either including or excluding non-primes.
#Much more can be read about the math behind this problem at:
#http://mathworld.wolfram.com/DecimalExpansion.html

import time
import os.path, sys
# An OS-independent hack for importing from the parent directory
sys.path.append(os.path.abspath(os.path.split(os.getcwd())[0]))
import pemaths

def findRecurrence(n):
    '''This method determines the length of the recurring cycle in a decimal
    expansion of the unit fraction 1/n.'''
    l = [1] # This is here by definition: unit fraction
    for exp in range(1, n):
        f = (10 ** exp) % n
        if not f:  # This is a terminating fraction.
            return 0
        elif f not in l:  # Have we encountered this remainder before?
            l.append(f)
        else:  # If we have seen this remainder before, we've completed a cycle
            s = l.index(f)  # Locate the first instance
            return (exp - s)  # The length of the cycle

def main():
    top = 1000
    #Routine for all n less than the top value
    longest = 0
    val = 0
    t = time.time()
    for num in range(2, top + 1):
        r = findRecurrence(num)
        if r > longest:
            longest = r
            val = num
    t = time.time() - t
    print('Including non-primes:')
    print(val)
    print('It took {0} seconds'.format(t))
    
    #Routine for all primes less than the top value
    longest = 0
    val = 0
    primes = pemaths.Eratosthenes(top)
    t = time.time()
    for num in primes:
        r = findRecurrence(num)
        if r > longest:
            longest = r
            val = num
    t = time.time() - t
    print('Using only primes:')
    print(val)
    print('It took {0} seconds'.format(t))
    
if __name__ == '__main__':
    main()