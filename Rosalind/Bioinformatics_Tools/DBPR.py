#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Introduction to Protein Databases

Usage:
  DNA.py <input>
  DNA.py (--help | --version)

Options:
  --compare       run a speed comparison of various methods
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Introduction to Protein Databases

Problem

The UniProt Knowledgebase can be found here.

You can see a complete description of a protein by entering its UniProt access
ID into the site's query field. Equivalently, you may simply insert its ID
(uniprot_id) directly into a UniProt hyperlink as follows:

http://www.uniprot.org/uniprot/uniprot_id
For example, the data for protein B5ZC00 can be found at
http://www.uniprot.org/uniprot/B5ZC00.

Swiss-Prot holds protein data as a structured .txt file. You can obtain it by
simply adding .txt to the link:

http://www.uniprot.org/uniprot/uniprot_id.txt
Given: The UniProt ID of a protein.

Return: A list of biological processes in which the protein is involved
(biological processes are found in a subsection of the protein's "Gene Ontology"
(GO) section).

Sample Dataset

H3SRW3

Sample Output

DNA recombination
DNA repair
SOS response
"""

from docopt import docopt
from Bio import ExPASy
from Bio import SwissProt


def get_uniprot_id_from_file(inp_file):
    with open(inp_file, 'r') as inp:
        return inp.readline().strip()


def main():
    #Grab our input id value
    uniprot_id = get_uniprot_id_from_file(arguments['<input>'])
    #Get a handle on the data for the uniprot id
    handle = ExPASy.get_sprot_raw(uniprot_id)
    #Parse our data
    record = SwissProt.read(handle)
    handle.close()
    #Process out the stuff of interest, GO values in this case
    go_refs = [ref[1:] for ref in record.cross_references if ref[0] == 'GO']
    for go_entry in go_refs:
        pre, val = go_entry[1].split(':')
        if pre == 'P':
            print(val)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()