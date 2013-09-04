#Problem 23 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#A perfect number is a number for which the sum of its proper divisors is
#exactly equal to the number. For example, the sum of the proper divisors of 28
#would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is less than n
#and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
#number that can be written as the sum of two abundant numbers is 24. By
#mathematical analysis, it can be shown that all integers greater than 28123
#can be written as the sum of two abundant numbers. However, this upper limit
#cannot be reduced any further by analysis even though it is known that the
#greatest number that cannot be expressed as the sum of two abundant numbers is
#less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of
#two abundant numbers.

import time

def pureAbundants(n):
    '''This function is a method for finding all abundant numbers up to N. It
    returns a list of only these numbers'''
    #findAbundants() below has some bloat added to facilitate later operations.
    pints = [1] * (n + 1)
    abundants = []
    for i in range(2, n / 2 + 1):
        for ind, val in enumerate(pints[2 * i::i]):
            pints[(ind + 2) * i] = val + i
    for ind, pint in enumerate(pints):
        if pint > ind:
            abundants += [ind]
    return abundants[1:]

def findAbundants():
    upper = 28123
    pints = [1] * (upper + 1)  # list for 0 and positive integers to upper limit
    for i in range(2, upper / 2 + 1):  # Note I already added 1 to everything
        for ind, val in enumerate(pints[2 * i::i]):
            pints[(ind + 2) * i] = val + i
    abundants = []  # A list for abundant numbers only
    cleaned = []  # A list where all non-abundant indices will hold 0 value
    for ind, pint in enumerate(pints):
        if pint > ind:
            cleaned += [ind]
            abundants += [ind]
        else:
            cleaned += [0]
    return cleaned, abundants[1:]

#The following strategy is one of the two I considered. In essence it tries each
#abundant number starting from 12 for substraction, then checks if the remainder
#is also an abundant number. If it is the sum of two abundant numbers, we
#would find out by n/2.
print('Using the first naive strategy:')
t = time.time()
numbers, abundantList = findAbundants()
print('Finding the abundant numbers took {0} seconds'.format(time.time() - t))
t = time.time()
#I create a variable to hold the sum of all numbers which are not the sum of two
#abundant numbers called sumNonSums
sumNonSums = sum(range(24))  # All the integers below 24 count towards the sum

for x in range(25, 28124):  # We shall consider all values from 25 to 28123
    for an in abundantList:
        if an > (x / 2):
            sumNonSums += x
            break
        else:
            if numbers[x - an]:
                break
print('Finding the sum of all numbers which are not the sum of two abundant \
numbers took {0} seconds'.format(time.time() - t))
print(sumNonSums)

#This is another strategy. It finds all combinations of two abundant numbers
#and removes them from a set of natural numbers. Everything that remains is thus
#not a sum of two natural numbers. There are 24,252,130 combinations, this will
#take a while, even though I shave off the ones that add to more than 28123
print('Using the second naive strategy (which shall take a little time):')
t = time.time()
abundantList = pureAbundants(28123)
print('Finding the abundant numbers took {0} seconds'.format(time.time() - t))
t = time.time()
naturals = range(28124)
for an in abundantList:
    for bn in abundantList:
        val = an + bn
        if val > 28123:
            break
        else:
            naturals[val] = 0
sumNonSums = sum(naturals)
print('Finding the sum of all numbers which are not the sum of two abundant \
numbers took {0} seconds'.format(time.time() - t))
print(sumNonSums)
