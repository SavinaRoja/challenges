#Problem 25 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#
#Hence the first 12 terms will be:
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the first term in the Fibonacci sequence to contain 1000 digits?
#
#This is simple enough to brute force
import time
LENGTH = 1000
maxval = 10 ** (LENGTH - 1)
print(maxval)
a = 0
b = 1
t = time.time()
cntr = 1
while b < maxval:
    a, b = b, a + b
    cntr += 1
print(cntr)
print("It took {0} seconds".format(time.time() - t))

#There are more intelligent ways of finding the answer, but I still need to
#prove them to myself before I implement them. Look into Binet's formula.