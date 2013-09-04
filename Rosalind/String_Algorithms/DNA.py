#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Counting DNA Nucleotides

Usage:
  DNA.py <input> [--compare]
  DNA.py (--help | --version)

Options:
  --compare       run a speed comparison of various methods
  -h --help       show this help message and exit
  -v --version    show version and exit

"""

problem_description = """Counting DNA Nucleotides

Problem

A string is simply an ordered collection of symbols selected from some alphabet
and formed into a word; the length of a string is the number of symbols that it
contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A',
'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string, s, of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21
"""

from docopt import docopt
from collections import Counter
from time import time


def get_string_from_dataset(inp_file):
    #The dataset should be a file with a single line, containing no more than
    #1000 characters of the ACGT alphabet
    with open(inp_file, 'r') as inp:
        data_string = inp.readline()
    return data_string


#I found this to be slowest
def counter_method(data):
    """Uses the collections module's Counter class"""
    count = Counter(data)
    return count['A'], count['C'], count['G'], count['T']


#Not as fast as string_count_method
def iter_bin_method(data):
    """Simple implementation of string iteration and binning"""
    a, c, g, t = 0, 0, 0, 0
    for char in data.strip():
        if char == 'A':
            a += 1
        elif char == 'C':
            c += 1
        elif char == 'G':
            g += 1
        else:
            t += 1
    return a, c, g, t


#I found this to be fastest
def string_count_method(data):
    '''Uses the string datatype's .count() methods '''
    return data.count('A'), data.count('C'), data.count('G'), data.count('T')

def main():
    """This will solve the problem, simply uses the iter_bin_method"""
    data_string = get_string_from_dataset(arguments['<input>'])
    a, c, g, t = iter_bin_method(data_string)
    print('{0} {1} {2} {3}'.format(a, c, g, t))


def compare():
    """
    This will seek to compare the collections.Counter datatype method to the
    iter_bin_method
    """
    data_string = get_string_from_dataset(arguments['<input>'])

    start = time()
    for i in range(1000):
        iter_bin_method(data_string)
    print('''It took the string-iteration binning method {0} seconds to \
complete 1000 repetitions\n'''.format(time() - start))

    start = time()
    for i in range(1000):
        counter_method(data_string)
    print('''It took the collections.Counter method {0} seconds to complete \
1000 repetitions\n'''.format(time() - start))

    start = time()
    for i in range(1000):
        string_count_method(data_string)
    print('''It took the ''.count() method {0} seconds to complete 1000 \
repetitions\n'''.format(time() - start))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()