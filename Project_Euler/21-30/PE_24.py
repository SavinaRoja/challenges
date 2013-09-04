#Problem 24 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#A permutation is an ordered arrangement of objects. For example, 3124 is one
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
#are listed numerically or alphabetically, we call it lexicographic order. The
#lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
#6, 7, 8 and 9?
#
#This one might be solved with relatively little programming. Let's examine
#that option first.
#
#There are 9! (=362880) options where 0 is the first digit.
#There are another 9! options where 1 is the first digit.
#Thus the first 725760 lexicographic options fall below the millionth term and
#I will ignore them. Where 2 is the first digit, we will find the millionth one.
#The 725761st term is thus 2013456789; for each iteration of a fixed second
#digit, 8! options (0, 1, 3, 4, 5, 6, 7, 8, 9) are explored, we want the one
#nearest and less than one million: giving us 27-------- (2*9! + 6*8! = 967680)
#and the remaining options of 0, 1, 3, 4, 5, 6, 8, and 9.
#Continuing this logic for the next digit: (2*9! + 6*8! + 6*7! = 967680)
#278------- : 0, 1, 3, 4, 5, 6, 9 --> 967680
#2783------ : 0, 1, 4, 5, 6, 9 --> 999360
#27839----- : 0, 1, 4, 5, 6 --> 999840
#278391---- : 0, 4, 5, 6 -- > 999984
#2783915--- : 0, 4, 6 --> 999996
#27839154-- : 0, 6 --> 999998  Only two steps away, only two ways of sorting
#2783915460 : Choosing the latter for the answer

#I could write a program to do this
import time
import math

t = time.time()
digits = range(10)
size = len(digits)
nthTerm = 1000000
answer = ''
for d in xrange(1, size):
    constant = 0
    val = math.factorial(size - d) * constant
    while val < nthTerm:
        constant += 1
        val = math.factorial(size - d) * constant
    constant -= 1
    val = math.factorial(size - d) * constant
    nthTerm -= val
    answer += str(digits.pop(constant))
    print(answer, nthTerm)
answer += str(digits[0])
print('The answer is {0}: {1} seconds'.format(answer, time.time() - t))

#I located the following code by Zachary Denton on eir blog which demonstrates
#the use of the standard python library. I'll let the tools stand for themselves
#and you can investigate them as I did.
#http://zacharydenton.com/project-euler-solutions/24/
from itertools import islice, permutations

print('Zachary Denton\'s solution:')  # Code I added for crediting
t = time.time()  # Code I added for built-in timing
print ''.join(next(islice(permutations(map(str, range(10))), 999999, None)))
print('{0} seconds'.format(time.time() - t)) # Code I added for built-in timing
