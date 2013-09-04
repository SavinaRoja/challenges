#Problem 21 from Project Euler
#Solution by Paul Barton
#
#Here is the text of the problem:
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#which divide evenly into n). If d(a) = b and d(b) = a, where a  b, then a and
#b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
#and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.
#
#Based on what I have read thus far, there is no comprehensive way to find
#amicable numbers, so I shall consider a brute-force approach. An efficient
#technique of finding proper divisors is going to be critical.
#
#Prime factorization can produce the number of proper divisors. As before, I
#will use the Sieve of Eratosthenes to yield the potential primes in a given
#range.
#
#Here is an only somewhat naive solution, it was my first success. I should
#make a more compact and optimized version.
import time

def Eratosthenes(n):
    candidates = range(n+1)
    fin = int(n**0.5)
    #Loop over the candidates, marking out each multiple.
    #If the current candidate is already checked off then
    #continue to the next iteration.
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n/i - 1)  # This is an obscure python
        #list expression that returns a list [from 2*i by multiples of i to end]
    #Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

def checkDivisor(n, d):
    e = 0
    while not n % d:
        n = n / d
        e += 1
    return(n, d, e)
    
def primeFactorize(n, primes):
    if n == 1:
        return([[1,0]])
    factors = []
    for p in primes:
        if p <= n:
            res = checkDivisor(n, p)
            n = res[0]
            if res[2]:
                factors.append([res[1],res[2]])
        else:
            break
    return(factors)

def ProperDivisors(pfactors):
    p, e = pfactors[0]
    values = []
    for i in range(e + 1):
        if pfactors[1:]:
            for each in ProperDivisors(pfactors[1:]):
                values.append(p ** i * each)
        else:
            values.append(p ** i)
    return(values)

VALUE = 100000
t = time.time()

myprimes = Eratosthenes(VALUE)
print('Got Primes!')

amicables = []
candidates = range(2, VALUE / 10)
for c in candidates:
    if c:
        pfs = primeFactorize(c, myprimes)
        propdivs = ProperDivisors(pfs)
        csum = sum(propdivs[:-1])
        if csum == c:
            continue
        pfs = primeFactorize(csum, myprimes)
        propdivs = ProperDivisors(pfs)
        nsum = sum(propdivs[:-1])
        if nsum == c:
            amicables += [c, csum]
            try:
                candidates[csum - 2] = 0
            except IndexError:
                pass
        
print(sum(amicables))
print('Completed in {0} seconds'.format(time.time() - t))

#Jarjar's original solution, more naive, even slower. I made the code nicer
#because it was crappy, but I left efficiency unaltered.
from math import ceil
t = time.time()
SKIP = True  # Change this to False if you want to run it
def d(n):
    f = 0
    for i in range (1,int(ceil(n/2)+1)):
        if n%i is 0:
            f+=i
    return f

if not SKIP:
    sums = 0
    for a in range(1,10000):
        b = d(a)
        if a == d(b) and a != b:
            sum += a
    print(sums)
    print('Completed in {0} seconds'.format(time.time() - t))
    
#Hooked's solution. About 10 times faster execution for 10,000
#I still need to analyze it for speedups beyond using the square root of N
t = time.time()
def divsum(n):return sum([k+n/k for k in range(1,int(n**.5 + 1)) if n%k == 0])-n
sum([n for n in range(1,10000) if n==divsum(divsum(n)) if n!=divsum(n)])
print(time.time() - t)