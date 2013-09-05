#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Finding a Motif in DNA

Usage:
  SUBS.py <input> [--compare]
  SUBS.py (--help | --version)

Options:
  -c --compare    run a speed test to compare various methods
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Finding a Motif in DNA

Problem

Given two strings s and t, t is a substring of s if t is contained as a
contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to
its left, including itself (e.g., the positions of all occurrences of 'U' in
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the
starting and ending positions of the substring in s; for example, if s =
"AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will
have multiple locations in s if it occurs more than once as a substring of s
(see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset

GATATATGCATATACTT
ATAT

Sample Output

2 4 10

Note:
The information above uses 1-based numbering for the indices of strings, as well
as an inclusive final index. This is contrary to python convention and results
in seemingly unusual index increments in the code.
"""

from docopt import docopt
from time import time


def get_sequence_and_query(inp_file):
    with open(inp_file, inp_file) as inp:
        sequence = inp.readline().strip()
        query = inp.readline().strip()
        if len(query) > len(sequence):
            raise ValueError('Query must be shorter than the searched sequence')
        return sequence, query


def findall(sequence, query):
    '''A custom method that relies on string.find, used as a generator'''
    offset = -1
    while True:  # We'll break on the sentinel value of string.find()
        offset = sequence.find(query, offset + 1)
        if offset == -1:
            break
        else:
            yield offset


def find_by_startswith(sequence, query):
    for offset in range(len(sequence)):
        if sequence[offset:].startswith(query):
            yield offset


def main():
    sequence, query = get_sequence_and_query(arguments['<input>'])
    offsets = ''
    for offset in findall(sequence, query):
        offsets += str(offset + 1) + ' '
    print(offsets)


def compare():
    """
    This will seek to compare the various solutions
    """
    sequence, query = get_sequence_and_query(arguments['<input>'])

    start = time()
    for i in range(1000):
        for x in findall(sequence, query):
            pass
    print('''It took the string.find iteration method {0} seconds to \
complete 1000 repetitions\n'''.format(time() - start))

    start = time()
    for i in range(1000):
        for x in find_by_startswith(sequence, query):
            pass
    print('''It took the find_by_startswith iteration method {0} seconds to \
complete 1000 repetitions\n'''.format(time() - start))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()