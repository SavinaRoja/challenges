#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Mortal Fibonacci Rabbits

Usage:
  FIBD.py <input>
  FIBD.py <n> <l> [<m>]
  FIBD.py (--help | --version)

Arguments:
  <input>         a filepath with containing k and n on the first line
                  separated by whitespace
  <n>             number of months that will pass
  <m>             number of months that a rabbit will live

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Mortal Fibonacci Rabbits

Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that
each pair of rabbits reaches maturity in one month and produces a single pair of
offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.

Sample Dataset

6 3

Sample Output

4
"""

from docopt import docopt
from itertools import islice


def get_n_m_from_input(inp_file):
    with open(inp_file, 'r') as inp:
        n, m = inp.readline().strip().split()
        return int(n), int(m)


def mortal_fibonacci(lifespan=3, maturation=1):
    '''
    This generator function implements a "mortal rabbit" fibonacci sequence.
    Lifespan determines how many intervals a rabbit will live, while
    maturation determines how many intervals it takes the rabbit to reach sexual
    maturity.

    Be aware that if lifespan<=maturation, your rabbits will die
    before they are able to reproduce. If maturation==0, then the rabbits will
    be able to reproduce as soon as they are born.
    '''
    #Population will represent our population in age intervals
    population = [0] * lifespan
    #The first interval: 1 pair young
    population[0] = 1
    yield sum(population)
    #Subsequent generations
    while True:
        population = [sum(population[maturation:])] + population[:-1]
        yield sum(population)


def main(n, m):
    if n is None and m is None:
        n, m = get_n_m_from_input(arguments['<input>'])
    else:
        n, m = int(n), int(m)
    val = islice(mortal_fibonacci(m), n - 1, n)
    print(val.next())


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main(arguments['<n>'], arguments['<m>'])
