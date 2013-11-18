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


def longest_common_subsequence(seq1, seq2):
    """
    This function returns the longest subsequence contained within both of the
    argument sequences. The term "sequence" is used in the sense of sequential
    data types such as lists, tuples, and strings. It may work with any data
    type that supports indexing and slicing.

    This function will return the longest subsequence(s) within as a set. If the
    sequences share no common subsequence, then the set will be empty.
    """
    def keyify(index1, index2):
        return str(index1) + str(index2)

    C = {}  # Common subsequence dict, stores previous checks
    longest_length = 0
    longest_common_subseq = set()
    for seq1_index, seq1_val in enumerate(seq1):
        for seq2_index, seq2_val in enumerate(seq2):
            if seq1_val == seq2_val:
                index_key = keyify(seq1_index, seq2_index)
                if seq1_index == 0 or seq2_index == 0:
                    length = 1
                else:
                    length = C.get(keyify(seq1_index - 1, seq2_index - 1), 0) + 1
                C[index_key] = length
                subseq = seq1[seq1_index - length + 1: seq1_index + 1]
                if length > longest_length:
                    longest_length = length
                    longest_common_subseq = set([subseq])
                elif length == longest_length:
                    longest_common_subseq.add(subseq)
    return longest_common_subseq

def longest_common(seqs):
    #An alternative method that relies on starting from the largest possible
    #subsequence and uses str.find() until found in all sequences
    #Not memory safe
    shortest = min(seqs, key=len)
    for length in xrange(len(shortest), 0, -1):
        for start in xrange(len(shortest) - length + 1):
            sub = shortest[start:start + length]
            if all(seq.find(sub) >= 0 for seq in seqs):
                return sub
    return ''

def main():
    #Get a generator of the sequences input
    sequences = SeqIO.parse(arguments['<input>'], 'fasta')
    seqs = [i.seq.tostring() for i in sequences]
    print(longest_common(seqs))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
