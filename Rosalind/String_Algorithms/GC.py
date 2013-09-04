#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Counting DNA Nucleotides

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




if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['--compare']:
        compare()
    else:
        main()
