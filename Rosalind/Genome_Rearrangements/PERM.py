#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Enumerating Gene Orders

Usage:
  PERM.py <input>
  PERM.py (--help | --version)

Arguments:
  <input>         a filepath with containing k and n on the first line
                  separated by whitespace
  <n>             number of months that will pass
  <m>             number of months that a rabbit will live

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Enumerating Gene Orders

Problem

A permutation of length n is an ordering of the positive integers {1,2,…,n}. For
example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).

Sample Dataset

3

Sample Output

6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

from docopt import docopt
import math


def get_n_from_input(inp_file):
    with open(inp_file, 'r') as inp:
        n = inp.readline().strip()
        return int(n)



def get_permutations(string, prefix=""):
    if len(string) == 1:
        yield prefix + string
    else:
        for i in range(len(string)):
            for perm in get_permutations(string[:i] + string[i+1:], prefix+string[i]):
                yield perm

def main():
    n = get_n_from_input(arguments['<input>'])
    #Finding the permuations of range(n) is trivial
    total = math.factorial(n)
    print(total)

    initial = ''.join([str(i) for i in range(1, n + 1)])
    for perm in get_permutations(initial):
        #Print with inserted spaces... apparently necessary
        spaced_perm = ''
        for char in perm:
            spaced_perm += char + ' '
        print(spaced_perm.rstrip())

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()