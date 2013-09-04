#Problem 18 from Project Euler
#Solution by Paul Barton
#
#The problem presents us with a triangle, which I represent as a list of lists
#in the code the below. Though this problem *may* be brute forced, I would like
#to do this problem elegantly the first time through, as it is merely a scaled
#down version of one which is not brute-forceable later on (#67).
#Thus we need a method that scales well.
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
#And so it goes... I think that perhaps this problem could be done in reverse.
#I will have to look into it. Intuitively, it might be even faster.


import time

TRIA = [[75],[95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28,
        6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33,
        47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17,
        14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73,
        16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53,
        60, 4, 23]]

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