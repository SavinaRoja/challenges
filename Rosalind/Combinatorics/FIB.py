#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rabbits and Recurrence Relations

Usage:
  FIB.py <input>
  FIB.py <n> <k>
  FIB.py (--help | --version)

Arguments:
  <input>         a filepath with containing k and n on the first line
                  separated by whitespace
  <n>             number of months that will pass
  <k>             number of pairs born in each litter to mature adults

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Rabbits and Recurrence Relations

Problem

A sequence is an ordered collection of objects (usually numbers), which are
allowed to repeat. Sequences can be finite or infinite. Two examples are the
finite sequence (π,−2√,0,π) and the infinite sequence of odd numbers
(1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect
to the values of previous terms. In the case of Fibonacci's rabbits from the
introduction, any given month will contain the rabbits that were alive the
previous month, plus any new offspring. A key observation is that the number of
offspring in any month is equal to the number of rabbits that were alive two
months prior. As a result, if Fn represents the number of rabbit pairs alive
after the n-th month, then we obtain the Fibonacci sequence having terms Fn that
are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate
the sequence). Although the sequence bears Fibonacci's name, it was known to
Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we
can simply use the recurrence relation to generate terms for progressively
larger values of n. This problem introduces us to the computational technique of
dynamic programming, which successively builds up solutions by using the answers
to smaller cases.

Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that will be present after n months if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset

5 3

Sample Output

19
"""

def get_k_n_from_input(inp_file):
    with open(inp_file, 'r') as inp:
        n, k = inp.readline().strip().split()
        return int(n), int(k)

from docopt import docopt

#This problem could be solved by recursion, but I'll implement a generator so as
#to avoid any possible problems with recursion limits
def modified_fibonacci(litter_pairs):
    #The first generation: 1 pair
    a = 1
    yield a
    #The second generation: 1
    b = 1
    yield b
    #All subsequent generations
    while True:
        a, b = b, a * litter_pairs + b
        yield b


def main(n, k):
    if n is None and k is None:
        n, k = get_n_k_from_input(arguments['<input>'])
    else:
        n, k = int(n), int(k)
    f = modified_fibonacci(k)
    for i in range(n):
        pop = f.next()
    print(pop)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main(arguments['<n>'], arguments['<k>'])
