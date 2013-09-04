#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Complementing a Strand of DNA

Usage:
  DNA.py <input>
  DNA.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Complementing a Strand of DNA

Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C'
and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing
the symbols of s, then taking the complement of each symbol (e.g., the reverse
complement of "GTCA" is "TGAC").

Given: A DNA string, s, of length at most 1000 bp.

Return: The reverse complement, sc, of s.

Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT
"""

from docopt import docopt


def get_string_from_dataset(inp_file):
    #The dataset should be a file with a single line, containing no more than
    #1000 characters of the ACGT alphabet
    with open(inp_file, 'r') as inp:
        data_string = inp.readline()
    return data_string.strip()


def reverse_complement(sequence):
    comp_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rev_comp = ''
    for char in sequence[::-1]:
        rev_comp += comp_dict[char]
    return rev_comp


def main():
    data_seq = get_string_from_dataset(arguments['<input>'])
    print(reverse_complement(data_seq))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
