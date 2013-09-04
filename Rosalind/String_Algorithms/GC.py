#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Computing GC Content

Usage:
  DNA.py <input>
  DNA.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Computing GC Content

Problem

The GC-content of a DNA string is given by the percentage of symbols in the
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A
commonly used method of string labeling is called FASTA format. In this format,
the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first
line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and
9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.

Sample Dataset

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output

Rosalind_0808
60.919540
"""

from docopt import docopt


def parse(inp_file):
    '''
    Parses the input file for the FASTA sequences, returning a list of two
    element tuples (name, sequence)
    '''
    with open(inp_file, 'r') as inp:
        lines = [line.strip() for line in inp.readlines()]
    sequences = []
    current_title = None
    for line in lines:
        if line.startswith('>'):
            if current_title is None:
                seq = ''
            else:
                sequences.append((current_title, seq))
                seq = ''
            current_title = line[1:]
        else:
            seq += line
    sequences.append((current_title, seq))
    return sequences

def calc_gc_percent(sequence):
    gc_frac = float(sequence.count('C') + sequence.count('G')) / len(sequence)
    return gc_frac * 100

def main():
    sequences = parse(arguments['<input>'])
    max_gc_val = 0
    max_gc_title = ''
    for seq_title, seq in sequences:
        gc_cont = calc_gc_percent(seq)
        if gc_cont > max_gc_val:
            max_gc_val = gc_cont
            max_gc_title = seq_title
    print(max_gc_title)
    print(max_gc_val)




if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
