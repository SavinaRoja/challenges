#Problem 4 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

import time

DIGITS = 3

s = 10 ** (DIGITS - 1) + 1
e = 10 ** DIGITS
greatestval = 0

def isPalindrome(inputstr):
    c = 0
    while c < (len(inputstr) / 2):
	if not inputstr[c] == inputstr[-(c + 1)]:
	    return False
	c += 1
    return True

t = time.time()

for j in range(s, e):
    for k in range(s, e):
	val = j * k
        if isPalindrome(str(val)) and val > greatestval:
            greatestval = val
print(greatestval)
print(time.time() - t)
