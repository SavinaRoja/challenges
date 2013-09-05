#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Locating Restriction Sites

Usage:
  DNA.py <input> [--compare]
  DNA.py (--help | --version)

Options:
  --compare       run a speed comparison of various methods
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Locating Restriction Sites

Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement.
For instance, GCATGC is a reverse palindrome because its reverse complement is
GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.

Sample Dataset

>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output

4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

from docopt import docopt
from time import time


def parse_fasta_sequence(inp_file):
    with open(inp_file, 'r') as inp:
        name = inp.readline().strip()[1:]
        sequence = ''
        for line in inp.readlines():
            sequence += line.strip()
    return name, sequence


def palindromes_by_nuclei(sequence, min_pal=4, max_pal=12):
    '''
    Checks for reverse palindromes in a DNA sequence; acts as a generator that
    will yield the starting offset of a palindrome along with its length.
    '''
    comp_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for offset in range(len(sequence)):
        mod = 0
        #Length is twice the mod value
        try:
            while sequence[offset - mod] == comp_dict[sequence[offset + mod + 1]]:
                mod += 1
                if mod * 2 >= min_pal:
                    yield offset - mod + 1, mod * 2
                if mod * 2 >= max_pal or offset - mod < 0:
                    break
        except IndexError:  # Expanded past sequence length
            pass


def main():
    name, sequence = parse_fasta_sequence(arguments['<input>'])
    for offset, length in palindromes_by_nuclei(sequence):
        print('{0} {1}'.format(offset + 1, length))


def compare():
    name, sequence = parse_fasta_sequence(arguments['<input>'])

    start = time()
    for i in range(100):
        for offset, length in palindromes_by_nuclei(sequence):
            pass
    print('''It took {0} seconds to complete 100 iterations of the Palindrome
by Nuclei search.\n'''.format(time() - start))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()
