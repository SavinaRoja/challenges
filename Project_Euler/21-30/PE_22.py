#Problem 22 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#containing over five-thousand first names, begin by sorting it into
#alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name
#score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is
#worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
#obtain a score of 938 * 53 = 49714.
#
#What is the total of all the name scores in the file?
#
#This problem is not terribly interesting mathematically, but it is a good way
#to increase one's domain knowledge of python. Here's a solution:

import string
import time

def score(name_string, mult, chars=string.ascii_uppercase):
    #This function will map the characters to their ASCII index values, sum for
    #each character, then multiply the total by the mulitplier and return
    val = 0
    for letter in name_string:
        val += chars.index(letter) + 1
    if name_string == 'COLIN':  # Check the method against the example rules
        print(name_string, val, mult, val * mult)
    return val * mult

t = time.time()
total = 0
with open('names.txt', 'r') as textfile:
    textline = textfile.read()
    #Each name has double quotes and is separate by commas, I don't want them
    names = textline.split('\",\"')
    names[0] = names[0][1:]  # Remove the start quote
    names[-1] = names[-1][:-1]  # Remove the end quote
    names.sort()  # Built-in sorting function to alphabetize
    for mult in range(1, len(names) + 1):
        total += score(names[mult - 1], mult)

print('The answer is: {0}'.format(total))
print('It took {0} seconds'.format(time.time() - t))
        
        
