#Problem 15 from Project Euler
#
#Solution by Paul Barton
#
#The problem outlines a 2 dimensional space of 21 nodes by 21 nodes, or 20 boxes
#by 20 boxes. It asks how many distinct paths may be taken without backtracking.
#
#It appears that backtracking is counter-intuitively defined as moving away from
#the end point, or in a negative fashion, rather than visiting the same node
#twice. This is makes it way the hell simpler...
#
#After fiddling around with this on paper, I have realized that this comes down
#to Pascal's triangle. It's an interesting demonstration of a property, but I
#went down the wrong road for a while due to misunderstanding the question.
#I considered the alternative (and also interesting) problem of how many unique
#paths there are to be explored in the space without visiting the same node more
#than once on a single path. I may work on that on my own...
#
#For the time being, here is a quick Pascal's Triangle generator and
#a print of the answer.
#Take a look at Pascal's Triangle and note that each value happens to represent
#the number of paths that exist to get there from the apex.

import time

t = time.time()

def pascal_tri(triangle=[[1]], control = 41):
    '''Returns a list of lists corresponding to layers of the pascal triangle.
    If you provide a custom start, know that garbage in will give you garbage
    out.'''
    while len(triangle) < control:
        previous_layer = triangle[-1]
        sum_list = []
        v = 0
        while v < len(previous_layer) - 1:
            sum_list.append(previous_layer[v] + previous_layer[v + 1])
            v += 1
        new_layer = [1] + sum_list + [1]
        triangle.append(new_layer)
        triangle = pascal_tri(triangle, control)
    return triangle

print('The answer is {0}'.format(pascal_tri()[40][20]))
print('It took {0} seconds'.format(time.time() - t))

#I determined that a problem I just worked out earlier today for a binomial
#distribution is related to Pascal's Triangle. Here is a quick explanation of why.
#On the grid, we can move either down or right, but not left or up.
#Based on the problem's restrictions, it will always take 40 "moves" to get to
#the end. This is a binomial choice.
#
#If one decided to review some good old combinations and permutations math:
#http://www.mathsisfun.com/combinatorics/combinations-permutations.html
#We have the problem of how many different combinations exist of either left or
#down moves in a set of 40 moves.
#Since we must have 20 down moves (or 20 right moves), how many ways can we
#combine these moves within a space of 40 moves. We shall use:
#The Binomial Coefficient
#  (N!)/((R!)(N-R!))

import math

s = time.time()

N = 40
R = 20
C = math.factorial(N)/(math.factorial(R) * math.factorial(N - R))

print('The answer is {0}'.format(C))
print('It took {0} seconds'.format(time.time() - s))
