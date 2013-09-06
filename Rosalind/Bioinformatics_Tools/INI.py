#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Introduction to the Bioinformatics Armory

Usage:
  DNA.py <input> [--compare]
  DNA.py (--help | --version)

Options:
  --compare       run a speed comparison of various methods
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Introduction to the Bioinformatics Armory

Problem

This initial problem is aimed at familiarizing you with Rosalind's task-solving
pipeline. To solve it, you merely have to take a given DNA sequence and find its
nucleotide counts; this problem is equivalent to “Counting DNA Nucleotides” in
the Stronghold.

Of the many tools for DNA sequence analysis, one of the most popular is the
Sequence Manipulation Suite. Commonly known as SMS 2, it comprises a collection
of programs for generating, formatting, and analyzing short strands of DNA and
polypeptides.

One of the simplest SMS 2 programs, called DNA stats, counts the number of
occurrences of each nucleotide in a given strand of DNA. An online interface for
DNA stats can be found here.

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must
provide your answer in the format shown in the sample output below.

Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21
"""

from docopt import docopt
from time import time
from Bio.Seq import Seq


def get_string_from_dataset(inp_file):
    #The dataset should be a file with a single line, containing no more than
    #1000 characters of the ACGT alphabet
    with open(inp_file, 'r') as inp:
        data_string = inp.readline()
    return data_string.strip()


def string_count_method(data):
    '''Uses the string datatype's .count() methods '''
    return data.count('A'), data.count('C'), data.count('G'), data.count('T')


def bio_seq_count_method(data):
    '''
    Uses the count method on the Seq class from BioPython. Includes
    instantiation of the class.
    '''
    dna = Seq(data)
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')

def bio_seq_without_instantiation(dna):
    '''BioPython Seq counting, but accepts already instantiated Seq'''
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')


def main():
    sequence = get_string_from_dataset(arguments['<input>'])
    print('{0} {1} {2} {3}'.format(*bio_seq_count_method(sequence)))


def compare():
    sequence = get_string_from_dataset(arguments['<input>'])

    start = time()
    for i in range(1000):
        string_count_method(sequence)
    print('''It took the string.count method {0} seconds to complete 1000 \
repetitions\n'''.format(time() - start))

    start = time()
    for i in range(1000):
        bio_seq_count_method(sequence)
    print('''It took the BioPython Seq.count method {0} seconds to complete \
1000 repetitions\n'''.format(time() - start))

    dna = Seq(sequence)
    start = time()
    for i in range(1000):
        bio_seq_without_instantiation(dna)
    print('''It took the BioPython Seq.count method {0} seconds to complete \
1000 repetitions without instantiating the sequence\n'''.format(time() - start))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()

