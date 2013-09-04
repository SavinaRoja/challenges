#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Transcribing DNA into RNA

Usage:
  DNA.py <input> [--compare]
  DNA.py (--help | --version)

Options:
  --compare       run a speed comparison of various methods
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Transcribing DNA into RNA

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G',
and 'U'.

Given a DNA string, t, corresponding to a coding strand, its transcribed RNA
string, u, is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset

GATGGAACTTGACTACGTAAATT

Sample Output

GAUGGAACUUGACUACGUAAAUU
"""

from docopt import docopt
from time import time


def get_string_from_dataset(inp_file):
    #The dataset should be a file with a single line, containing no more than
    #1000 characters of the ACGT alphabet
    with open(inp_file, 'r') as inp:
        data_string = inp.readline()
    return data_string.strip()


def string_replace_method(data):
    return data.replace('T', 'U')


def iterative_transcribe_method(data):
    rna = ''
    for char in data:
        if char == 'T':
            rna += 'U'
        else:
            rna += char
    return rna


def main():
    """This will solve the problem, simply uses the string_replace_method"""
    data_string = get_string_from_dataset(arguments['<input>'])
    print(string_replace_method(data_string))


def compare():
    """
    This will seek to compare the various solutions
    """
    data_string = get_string_from_dataset(arguments['<input>'])

    start = time()
    for i in range(1000):
        string_replace_method(data_string)
    print('''It took the string_replace method {0} seconds to complete 1000 \
repetitions\n'''.format(time() - start))

    start = time()
    for i in range(1000):
        iterative_transcribe_method(data_string)
    print('''It took the string_replace method {0} seconds to complete 1000 \
repetitions\n'''.format(time() - start))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()
