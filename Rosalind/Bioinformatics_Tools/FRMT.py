#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Data Formats

Usage:
  FRMT.py <input> <email>
  FRMT.py (--help | --version)

Arguments:
  <input>         A file with space separated GenBank IDs on a single line.
  <email>         An email address for the submission of requests to Entrez.

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Data Formats

Problem

GenBank can be accessed here (http://www.ncbi.nlm.nih.gov/genbank/). A detailed
description of the GenBank format can be found here
(http://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html). A tool, from the SMS 2
package, for converting GenBank to FASTA can be found here
(http://www.bioinformatics.org/sms2/genbank_fasta.html).

Given: A collection of n (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.

Sample Dataset

FJ817486 JX069768 JX469983

Sample Output

>gi|408690371|gb|JX469983.1| Zea mays subsp. mays clone UT3343 G2-like \
transcription factor mRNA, partial cds
ATGATGTATCATGCGAAGAATTTTTCTGTGCCCTTTGCTCCGCAGAGGGCACAGGATAATGAGCATGCAA
GTAATATTGGAGGTATTGGTGGACCCAACATAAGCAACCCTGCTAATCCTGTAGGAAGTGGGAAACAACG
GCTACGGTGGACATCGGATCTTCATAATCGCTTTGTGGATGCCATCGCCCAGCTTGGTGGACCAGACAGA
GCTACACCTAAAGGGGTTCTCACTGTGATGGGTGTACCAGGGATCACAATTTATCATGTGAAGAGCCATC
TGCAGAAGTATCGCCTTGCAAAGTATATACCCGACTCTCCTGCTGAAGGTTCCAAGGACGAAAAGAAAGA
TTCGAGTGATTCCCTCTCGAACACGGATTCGGCACCAGGATTGCAAATCAATGAGGCACTAAAGATGCAA
ATGGAGGTTCAGAAGCGACTACATGAGCAACTCGAGGTTCAAAGACAACTGCAACTAAGAATTGAAGCAC
AAGGAAGATACTTGCAGATGATCATTGAGGAGCAACAAAAGCTTGGTGGATCAATTAAGGCTTCTGAGGA
TCAGAAGCTTTCTGATTCACCTCCAAGCTTAGATGACTACCCAGAGAGCATGCAACCTTCTCCCAAGAAA
CCAAGGATAGACGCATTATCACCAGATTCAGAGCGCGATACAACACAACCTGAATTCGAATCCCATTTGA
TCGGTCCGTGGGATCACGGCATTGCATTCCCAGTGGAGGAGTTCAAAGCAGGCCCTGCTATGAGCAAGTC
A
"""

from docopt import docopt
from Bio import Entrez
from Bio import SeqIO


def get_ids_from_file(inp_file):
    with open(inp_file, 'r') as inp:
        genbank_ids = inp.readline().strip().split(' ')
    return genbank_ids


def main():
    genbank_ids = get_ids_from_file(arguments['<input>'])
    Entrez.email = arguments['<email>']

    #Get the results in FASTA form and parse them with SeqIO
    handle = Entrez.efetch(db='nucleotide', id=','.join(genbank_ids),
                           rettype='fasta')
    records = SeqIO.parse(handle, 'fasta')

    #Find the shortest
    shortest = (None, None)
    for record in records:
        if len(record.seq) < shortest[0] or shortest[0] is None:
            shortest = (record.seq, record.description)

    #Print the results
    print('>' + shortest[1])
    print(shortest[0])


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
