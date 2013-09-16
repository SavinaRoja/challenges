#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Translating RNA into Protein

Usage:
  PROT.py <input>
  PROT.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Translating RNA into Protein

Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from
the English alphabet (all letters except for B, J, O, U, X, and Z). Protein
strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10
kbp).

Return: The protein string encoded by s.

Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING
"""

from docopt import docopt
from itertools import tee, izip


#Itertools recipe
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

codons = '''\
UUU F    CUU L    AUU I    GUU V    UAU Y     CAU H    AAU N    GAU D  \
UUC F    CUC L    AUC I    GUC V    UAC Y     CAC H    AAC N    GAC D  \
UUA L    CUA L    AUA I    GUA V    UAA Stop  CAA Q    AAA K    GAA E  \
UUG L    CUG L    AUG M    GUG V    UAG Stop  CAG Q    AAG K    GAG E  \
UCU S    CCU P    ACU T    GCU A    UGU C     CGU R    AGU S    GGU G  \
UCC S    CCC P    ACC T    GCC A    UGC C     CGC R    AGC S    GGC G  \
UCA S    CCA P    ACA T    GCA A    UGA Stop  CGA R    AGA R    GGA G  \
UCG S    CCG P    ACG T    GCG A    UGG W     CGG R    AGG R    GGG G  \
'''
codon_table = {}
for key, val in pairwise(codons.split()):
    codon_table[key] = val


def get_rna_string(inp_file):
    with open(inp_file, 'r') as inp:
        rna = inp.readline().strip()
    return rna


def reverse_complement(sequence):
    comp_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    rev_comp = ''
    for char in sequence[::-1]:
        rev_comp += comp_dict[char]
    return rev_comp


def translate_until_stop(rna):
    '''
    This will translate an RNA sequence into protein until a stop codon is
    reached or the end of the sequence is reached.
    '''
    protein = ''
    index = 0
    while True:
        try:
            amino_acid = codon_table[rna[index:index + 3]]
        except IndexError:
            return protein
        except KeyError:
            return protein
        if amino_acid == 'Stop':
            return protein
        protein += amino_acid
        index += 3


def get_ORFs(rna):
    '''
    This function will attempt to translate the RNA to protein for all ORFs in
    the sequence as well as its reverse complement. Each translated sequence
    will be returned along with its starting position, ending position, and
    strand information.

    Returns: (protein_sequence, rna_start, rna_strand)
    '''
    translations = []
    rna_length = len(rna)
    starts = []
    for i in range(rna_length):
        if rna[i:i + 3] == 'AUG':
            starts.append(i)
    for start in starts:
        protein = translate_until_stop(rna[start:])
        translations.append((protein, start, "5'3'"))

    #Now time to do the same for the reverse complement
    revcomp_rna = reverse_complement(rna)
    starts = []
    for i in range(rna_length):
        if revcomp_rna[i:i + 3] == 'AUG':
            starts.append(i)
    for start in starts:
        protein = translate_until_stop(revcomp_rna[start:])
        #The end of the revcomp will be our start
        end = start + len(protein) * 3
        translations.append((protein, rna_length - end, "3'5'"))
    return translations


def main():
    rna = get_rna_string(arguments['<input>'])
    results = get_ORFs(rna)
    #We only need the first of our results, solution is overly general
    print(results[0][0])

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
