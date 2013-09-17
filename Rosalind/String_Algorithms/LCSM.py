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

A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible; in this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
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
    #Use SeqIO to get an iterator over the input sequences
    records = SeqIO.parse(arguments['<input>'], 'fasta')
    #We'll need a means to track counts-by-index, but length is as yet unknown
    count = None
    for fasta in records:
        seq = fasta.seq
        sl = len(seq)
        if count is None:
            #A sequence-length list of 4-length lists
            count = [list(a) for a in zip([0]*sl, [0]*sl, [0]*sl, [0]*sl)]
        for index in range(sl):
            if seq[index] == 'A':
                count[index][0] += 1
            elif seq[index] == 'C':
                count[index][1] += 1
            elif seq[index] == 'G':
                count[index][2] += 1
            elif seq[index] == 'T':
                count[index][3] += 1
    #Get the consensus sequence
    consensus = ''.join(['ACGT'[i.index(max(i))] for i in count])
    print(consensus)
    #These will not look pretty with a larger number of sequences
    print('A: ' + ' '.join([str(i[0]) for i in count]))
    print('C: ' + ' '.join([str(i[1]) for i in count]))
    print('G: ' + ' '.join([str(i[2]) for i in count]))
    print('T: ' + ' '.join([str(i[3]) for i in count]))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
