#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Finding a Motif in DNA

Usage:
  SUBS.py <input>
  SUBS.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Finding a Motif in DNA

Problem

Given two strings s and t, t is a substring of s if t is contained as a
contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to
its left, including itself (e.g., the positions of all occurrences of 'U' in
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the
starting and ending positions of the substring in s; for example, if s =
"AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will
have multiple locations in s if it occurs more than once as a substring of s
(see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset

GATATATGCATATACTT
ATAT

Sample Output

2 4 10

Note:
The information above uses 1-based numbering for the indices of strings, as well
as an inclusive final index. This is contrary to python convention and results
in seemingly unusual index increments in the code.
"""

from docopt import docopt


def findallsubstrings(string, substring):


def main():
    data_seq = get_string_from_dataset(arguments['<input>'])
    print(reverse_complement(data_seq))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()