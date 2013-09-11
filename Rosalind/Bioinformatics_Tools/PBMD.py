#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PubMed Search

Usage:
  DNA.py <input> <email>
  DNA.py (--help | --version)

Arguments:
  <input>         A file containing three lines corresponding to genus, starting
                  date, and ending date respectively.
  <email>         An email address for the submission of requests to Entrez.

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """PubMed Search

Problem

Here are two links for searching the PubMed database:

PubMed database, along with advanced search.
http://www.ncbi.nlm.nih.gov/pubmed/
http://www.ncbi.nlm.nih.gov/pubmed/advanced

List of Available Search Tags.
http://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descrip

Given: The surname and initials of an author, followed by a year.

Return: The PubMed identifier (PMID) of the first article published by this
author in the year specified.

Sample Dataset

Brent MR
2007

Sample Output

17210930
"""

from docopt import docopt
from Bio import Entrez
from datetime import date

SEARCH_FORM = '"{0}"[AU] AND ("{1}/1/1"[DP] : "{1}/12/31"[DP])'


def get_search_parameters(inp_file):
    with open(inp_file, 'r') as inp:
        name = inp.readline().strip()
        year = inp.readline().strip()
    return name, year


def parse_pubdate_string_to_ints(pubdate):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']
    #There should always be a year
    year, others = pubdate.split(' ')[0], pubdate.split(' ')[1:]
    year = int(year)
    #If the month or day do not exist, they will be 1 for our purposes
    #If we are given an interval, "May-Jun" or "12-17", the first will be used
    try:
        month = int(months.index(others[0].split('-')[0])) + 1
    except IndexError:
        month = 1
        day = 1
    except ValueError:
        seasons = {'Spring': 2,'Summer': 5, 'Fall':  8, 'Winter': 11}
        month = seasons[others[0]]
        day = 1
    else:
        try:
            day = int(others[1].split('-')[0])
        except IndexError:
            day = 1
    return year, month, day


def main():
    name, year = get_search_parameters(arguments['<input>'])
    Entrez.email = arguments['<email>']
    handle = Entrez.esearch(db='pubmed', term=SEARCH_FORM.format(name, year),
                            retmax=500)
    record = Entrez.read(handle)
    #As far as I know, there is no way to have esearch return a sorted list
    #Some documentation may be read here:
    #  http://www.ncbi.nlm.nih.gov/books/NBK25499/
    #So I iterate through the UIDs by summary and look for the earliest date
    earliest_date = (date.today(), None)
    for uid in record['IdList']:
        record = Entrez.read(Entrez.esummary(db='pubmed', id=uid))
        pubdate_str = record[0]['PubDate']
        year, month, day = parse_pubdate_string_to_ints(pubdate_str)
        pubdate = date(year, month, day)
        print(uid, pubdate)
        if pubdate < earliest_date[0]:
            earliest_date = (pubdate, uid)
    print(earliest_date[1])


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
