#Problem 13 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Work out the first ten digits of the sum of the following one-hundred 50-digit
#numbers.
#(Numbers stored in PE_13.txt)
#
#This is a fairly basic problem. The solution illustrates some basic Python
#file usage and string-integer conversion.

value = 0  # Create a value to hold the sum
with open('PE_13.txt','r') as f:  # This loop will close the file when exiting
    for line in f.readlines():  # readlines() generates a list of file lines
        value += int(line.strip())  # strip() will remove the newline character
print(str(value)[:10])  # Convert the integer sum to a string; then print soln.

