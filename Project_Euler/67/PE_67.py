#Problem 67 from Project Euler
#Solution by Paul Barton
#
#This problem is the problem from 15 scaled up to prevent brute-forcing methods.
#
#I observe that the algorithm has only limited need for memory. Each point has
#multiple routes to get to it, but only the one of highest value matters.
#
#    75                --                    --
#  95  64    -->    170  139    -->     ---       ---
#17  47  82       17   47   82      187    217/186   221
#
#On the third step we have a choice, there were multiple routes to this middle
#node, but the future choice space is the same, so why even think about the one
#that has a lesser value. I use only the highest valued history for the
#degenerate states in the future calculations. Thus the next step would be:
#
#  187  217   221             ---       ---       ---
#18   35   87   10   -->   205   222/252   304/308   231
#
#Many people on the Project Euler forum say that this can be done from the
#bottom up. This seems like a sound idea, I believe that that approach would
#be faster as it should require fewr comparisons. I will implement them in
#tandem later.

import time

TRIA = []
with open('triangle.txt', 'r') as inp:
    for line in inp.readlines():
        newlist = []
        for value in line.split(' '):
            newlist.append(int(value.rstrip()))
        TRIA.append(newlist)

t = time.time()

def compute_layer(top, bottom):
    '''I will do some stuff that might seem ugly, but it should be a little
    faster and still comprehensible.'''
    ind = 0
    layer = []
    while ind < len(bottom):
        if ind:
            f = top[ind - 1]
        else:
            f = 0
        try:
            s = top[ind]
        except IndexError:
            s = 0
        layer.append(max(f, s))
        ind += 1
    return layer

last = []
m = 0
while m < len(TRIA) - 1:
    if not last:
        last = compute_layer(TRIA[m], TRIA[m + 1])
    else:
        last = compute_layer(last, TRIA[m + 1])
    m += 1
    
print(max(last))
print(time.time() - t)