#Problem 8 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Find the greatest product of five consecutive digits in the 1000-digit number.
#    7316717653133...420752963450
#(I stored the full number in the text file named "PE_8.txt")
#
#My strategy is to simply parse the number into a list/string of single digits
#and calculate the products, keeping the largest number as I go along

import time

def digitsProduct(input_string):
    '''Accepts a string of digits to convert to integers; returns their product'''
    val = 1
    for digit in input_string:
        val = val * int(digit)
    return val

t = time.time()

with open('PE_8.txt', 'r') as mynum:
    n = mynum.read()

window = 5  # Set the window size, 5 for the described problem
greatest = 0  # Store greatest value

for i in xrange(len(n) - window + 1):  # Scan through the string
    val = digitsProduct(n[i: i + window])  # Product value
    if val > greatest:
        greatest = val

print('The greatest product of digits found was: {0}'.format(greatest))
print('This took {0} seconds'.format(time.time() - t))
    