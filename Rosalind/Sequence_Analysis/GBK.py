#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""GenBank Introduction

Usage:
  GBK.py <input> <email>
  GBK.py (--help | --version)

Arguments:
  <input>         A file containing three lines corresponding to genus, starting
                  date, and ending date respectively.
  <email>         An email address for the submission of requests to Entrez.

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """GenBank Introduction

Problem

GenBank comprises several subdivisions:

Nucleotide: a collection of nucleic acid sequences from several sources.
Genome Survey Sequence (GSS): uncharacterized short genomic sequences.
Expressed Sequence Tags, (EST): uncharacterized short cDNA sequences.
Searching the Nucleotide database with general text queries will produce the
most relevant results. You can also use a simple query based on protein name,
gene name or gene symbol.

To limit your search to only certain kinds of records, you can search using
GenBank's Limits page or alternatively use the Filter your results field to
select categories of records after a search.

If you cannot find what you are searching for, check how the database
interpreted your query by investigating the Search details field on the right
side of the page. This field automatically translates your search into standard
keywords.

For example, if you search for Drosophila, the Search details field will contain
(Drosophila[All Fields]), and you will obtain all entries that mention Drosophi
a (including all its endosymbionts). You can restrict your search to only
organisms belonging to the Drosophila genus by using a search tag and searching
for Drosophila[Organism].

Given: A genus name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were
published between the dates specified.

Sample Dataset

Anthoxanthum
2003/7/25
2005/12/27

Sample Output

7
"""

from docopt import docopt
from Bio import Entrez

#This problem involves some familiarity with Entrez's search, go here:
# http://www.ncbi.nlm.nih.gov/nuccore/advanced for an interactive builder

SEARCH_FORM = '''("{0}"[Organism]) AND ("{1}"[Publication Date] : \
"{2}"[Publication Date])'''


def get_search_parameters(inp_file):
    with open(inp_file, 'r') as inp:
        genus = inp.readline().strip()
        start_date = inp.readline().strip()
        end_date = inp.readline().strip()
    return genus, start_date, end_date


def main():
    genus, start, end = get_search_parameters(arguments['<input>'])
    Entrez.email = arguments['<email>']
    handle = Entrez.esearch(db='nucleotide',
                            term=SEARCH_FORM.format(genus, start, end))
    record = Entrez.read(handle)
    print(record['Count'])

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
