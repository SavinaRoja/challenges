#Problem 6 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#The sum of the squares of the first ten natural numbers is,
#
#1^(2) + 2^(2) + ... + 10^(2) = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^(2) = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural
#numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sum.
#
#Time to do some basic python math operations!
#Since the code will be so simple, I'll elaborate on the variable names
highest = 100
sum_of_squares = 0
sum_of_naturals = 0
square_of_sum = 0

for i in xrange(1, highest + 1):  # Do things in a single loop 
    sum_of_naturals += i  # We'll need this for the square of sum
    sum_of_squares += i ** 2  # We'll calculate sum of squares as we go
    
square_of_sum = sum_of_naturals ** 2
diff = square_of_sum - sum_of_squares
print('The difference is {0}'.format(diff))