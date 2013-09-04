#Problem 1 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we
#get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
#
#My first approach was to simply brute force it as it is a very simple problem.
#I calculated all of the multiples of three and five less than 999, then summed
#them and removed duplicate values. This is some code from my very early days
#of programming.

# all things below this value
VALUE = 999

# max multiplying integer of three
threemult = VALUE / 3

# max multiplying integer of five
fivemult = VALUE / 5

threes = []
fives = []

n = 0
while (n <= threemult):
   threes.append(n * 3)
   n += 1

n = 0
while (n <= fivemult):
    fives.append(n * 5)
    n += 1
    
total = sum(threes) + sum(fives)

for number in threes:
    if number in fives:
        total = total - number
        
print(total)

#There is another way to do this using a derived equation for a finite series
#in an arithmetic progression. The sum of an arithmetic progression can be shown
#to be:  Sn = n/2 * (a1 + an)
#Where a1 is the starting value of the progression and an is the final.
#Here I use this knowledge for a solution.

#We want to find the highest multiple for three and five for their arithmetic
#progressions.
fivetop = VALUE
threetop = VALUE
fifteentop = VALUE  # The LCM of 3 and 5
while fivetop % 5:
    fivetop -= 1
while threetop % 3:
    threetop -= 1
while fifteentop % 15:   # We can use this to create a series of common values
    fifteentop -= 1
    
#All of the stuff to add
mysum = ((threetop / 3) / 2.0) * (3 + threetop)
mysum += ((fivetop / 5) / 2.0) * (5 + fivetop)
#The stuff to substract
mysum -= ((fifteentop / 15) / 2.0) * (15 + fifteentop)

print(mysum)
    



