#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Finding a Shared Motif

Usage:
  LCSM.py <input>
  LCSM.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Finding a Shared Motif

Problem

A common substring of a collection of strings is a substring of every member of
the collection. We say that a common substring is a longest common substring if
there does not exist a longer common substring. For example, "CG" is a common
substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible; in
this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple
example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)
Sample Dataset

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output

AC
"""

from docopt import docopt
from Bio import SeqIO


def main():
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
