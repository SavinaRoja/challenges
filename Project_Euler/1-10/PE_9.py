#Problem 9 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^(2) + b^(2) = c^(2)
#For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import time

#Here is a fast brute force solution. It is optimized by restricting the range
#of potential C values to those allowed by the inequality constraints as well as
#keeping all sides equal to the triplet sum. A and B converge. Note that not all
#integers are sums of pythagorean triples.
tripletsum = 1000
#C cannot be greater than half the triplet sum, as A + B must be greater than C
C = tripletsum / 2
t = time.time()
while C >= (tripletsum / 3 + 1):  # C cannot be less than a third of the sum
    #B shall be the greater side, A the lesser
    A = 1
    B = tripletsum - C - A
    while (A <= (tripletsum - C)/2):
        if not ((A**2) + (B**2) - (C**2)):
            print('A: {0}, B: {1}, C: {2}'.format(A, B, C))
            print('The solution is {0}'.format(A * B * C))
            print('This brute-force took {0} seconds'.format(time.time() - t))
            break
        else:
            A += 1
            B -= 1
    C -= 1

#Here is another solution using Euclid's formula for pythagorean triples
#A = 2 * m * n
#B = m^(2) - n^(2)
#C = m^(2) + n^(2)
solved = False
t = time.time()
#It can be shown that m(m + n) = tripletsum / 2
half = tripletsum / 2
n = 1 #n must be at least 1
m = int(half ** 0.5) #m will at most be less than the square root of half
while m:
    n = 1
    while (m * (m + n)) <= half:
        if not half - (m * (m + n)):
            solved = True
            A = 2 * m * n
            B = m ** 2 - n ** 2
            C = m ** 2 + n ** 2
            print('A: {0}, B: {1}, C: {2}'.format(A, B, C))
            print('The solution is {0}'.format(A * B * C))
            print('Using Euclid\'s formula, it took {0} seconds'.format(time.time() - t))
            break
        n+= 1
    if solved:
        break
    m -= 1


