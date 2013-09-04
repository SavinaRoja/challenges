#Problem 28 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Starting with the number 1 and moving to the right in a clockwise direction a 5
#by 5 spiral is formed as follows:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#It can be verified that the sum of the numbers on the diagonals is 101.
#
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
#in the same way?
###
#The problem can be simplified in the following way: with a starting value of 1
#and an increment of 2, the next 4 values are found by applying the increment.
#Every 4 steps, the increment increases by 2. This is a fairly simple one.

import time

t = time.time()
MAX = 1001
n = 1
inc = 2
solution_sum = 1
while n < (MAX ** 2):
    for i in xrange(4):
        n += inc
        solution_sum += n
    inc += 2
print(solution_sum)
print('Solved in {0} seconds'.format(time.time() - t))