#Problem 20 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#n! means n * (n - 1) * ... * 3 * 2 * 1
#
#For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!
#
#The following brute force method took me about a minute to write, and another
#minute to prettify. It's pretty basic python string-int conversion.
import math
import time

t = time.time()
val = math.factorial(100)
strung = str(val)
count = 0
for char in strung:
    count += int(char)
print(count)
print('This took {0} seconds'.format(time.time() - t))