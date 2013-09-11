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
from collections import namedtuple

SEARCH_FORM = '"{0}"[AU] AND ("{1}/1/1"[DP] : "{1}/12/31"[DP])'

item_info = namedtuple('ItemInfo', 'pmid, pubdate, abbrev_journal_name')


def get_search_parameters(inp_file):
    with open(inp_file, 'r') as inp:
        name = inp.readline().strip()
        year = inp.readline().strip()
    return name, year


def parse_pubdate_string_to_ints(pubdate):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']
    seasons = {'Spring': 3, 'Summer': 6, 'Fall': 9, 'Winter': 12}
    #There should always be a year
    year, others = pubdate.split(' ')[0], pubdate.split(' ')[1:]
    year = int(year.split('-')[0])
    #If the month or day do not exist, they will be 1 for our purposes
    #If we are given an interval, "May-Jun" or "12-17", the first will be used
    try:
        month = int(months.index(others[0].split('-')[0])) + 1
    except IndexError:
        month = 1
        day = 1
    except ValueError:
        month = seasons[others[0]]
        day = 1
    else:
        try:
            day = int(others[1].split('-')[0])
        except IndexError:
            day = 1
    return year, month, day


def get_abbrev_journal_name(full_journal_name):
    handle = Entrez.esearch(db='journals', term=full_journal_name)
    record = Entrez.read(handle)
    summ_handle = Entrez.esummary(db='journals', id=record['IdList'][0])
    summ_record = Entrez.read(summ_handle)
    return summ_record[0]['MedAbbr']


def get_earliest_record(records):
    '''
    Looks for the namedtuple(pmid, pubdate, abbrev_journal_name) in a list with
    the following attributes, in order or priority:
      Lowest PubDate
      Highest alphabetical Abbreviated Journal Name
      Smallest PMID
    This record is then returned
    '''
    earliest = item_info(None, date.today(), None)
    for record in records:
        if record.pubdate < earliest.pubdate:  # Date order priority
            earliest = record
        elif record.pubdate == earliest.pubdate:
            #Journal name resolves ambiguity in equivalent dates
            if record.abbrev_journal_name > earliest.abbrev_journal_name:
                earliest = record
            elif record.abbrev_journal_name == earliest.abbrev_journal_name:
                #Resolving beyond this is undocumented by PubMed, but I observed
                #it with '"Lip GY"[AU] and "2012"[DP]', I used PMID to resolve
                #this last level of ambiguity, in accordance with observed datum
                if record.pmid < earliest.pmid:
                    earliest = record
    return earliest


def main():
    name, year = get_search_parameters(arguments['<input>'])
    Entrez.email = arguments['<email>']

    search = SEARCH_FORM.format(name, year)
    print('Conducting search of PubMed... {0}'.format(search))
    handle = Entrez.esearch(db='pubmed', term=search, retmax=500)
    record = Entrez.read(handle)

    #Get summaries for the results, using a list is nicer to the server
    print('Requesting summaries of matches...')
    uids = ','.join(record['IdList'])  # must be comma-separated vals, not list
    summary_handle = Entrez.esummary(db='pubmed', id=uids)
    summary_record = Entrez.read(summary_handle)

    #Extract the needed information for sorting and identification
    print('Parsing matches for dates, retrieving abbreviated journal names...')
    records = []
    for item in summary_record:
        pmid = item['ArticleIds']['pubmed'][0]
        year, month, day = parse_pubdate_string_to_ints(item['PubDate'])
        pubdate = date(year, month, day)
        full_journal_name = item['FullJournalName']
        abbrev_journal_name = get_abbrev_journal_name(full_journal_name)
        records.append(item_info(pmid, pubdate, abbrev_journal_name))

    #Now we can do search, by date, abbreviated journal name, then PMID
    print('Finding earliest result by: date, abbrev. journal name, PMID...')
    earliest = get_earliest_record(records)

    #Finally we can print our earliest publication
    print('PMID of earliest publication: {0}'.format(earliest.pmid))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
