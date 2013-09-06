#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Counting Point Mutations

Usage:
  DNA.py <input>
  DNA.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Counting Point Mutations

Problem

Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7
"""

from docopt import docopt


def get_sequences(inp_file):
    with open(inp_file, 'r') as inp:
        return inp.readline().strip(), inp.readline().strip()


def hamming_distance(seq1, seq2):
    '''
    Calculates the Hamming distance between two strings/sequences of equal
    length. This distance is the sum quantity of unique indices in the strings
    where those values are not equivalent.
    '''
    return sum([1 if seq1[i] != seq2[i] else 0 for i in range(len(seq1))])


def main():
    sequence1, sequence2 = get_sequences(arguments['<input>'])
    print(hamming_distance(sequence1, sequence2))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
