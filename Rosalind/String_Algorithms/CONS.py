#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Consensus and Profile

Usage:
  CONS.py <input>
  CONS.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Consensus and Profile

Problem

A matrix is a rectangular table of values divided into rows and columns. An m×n
matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the
value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number of
times that 'A' occurs in the jth position of one of the strings, P2,j represents
the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.

DNA Strings:
        A T C C A G C T
        G G G C A A C T
        A T G G A T C T
        A A G C A A C C
        T T G G A A C T
        A T G C C A T T
        A T G G C A C T

Profile:
    A   5 1 0 0 5 5 0 0
    C   0 0 1 4 2 0 6 1
    G   1 1 6 3 0 1 0 0
    T   1 5 0 0 0 1 1 6

Consensus:
        A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in
FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

Sample Dataset

>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output

ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

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
