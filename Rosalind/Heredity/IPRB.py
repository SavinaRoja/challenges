#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Mendel's First Law

Usage:
  IPRB.py <input>
  IPRB.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit
"""

problem_description = """Mendel's First Law
Problem

Probability is the mathematical study of randomly occurring phenomena. We will
model such a phenomenon with a random variable, which is simply a variable that
can take a number of different distinct outcomes depending on the result of an
underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If
we let X represent the random variable corresponding to the color of a drawn
ball, then the probability of each of the two outcomes is given by Pr(X=red)=35
and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the
ball example, let Y model the color of a second ball drawn from the bag (without
replacing the first ball). The probability of Y being red depends on whether the
first ball was red or blue. To represent all outcomes of X and Y, we therefore
use a probability tree diagram. This branching diagram represents all possible
individual probabilities for X and Y, with outcomes at the endpoints ("leaves")
of the tree. The probability of any outcome is given by the product of
probabilities along the path from the beginning of the tree; see Figure 2 for an
illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the
probability of an event can be written as the sum of the probabilities of its
constituent outcomes. For our colored ball example, let A be the event "Y is
blue." Pr(A) is equal to the sum of the probabilities of two different outcomes:
Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant
phenotype). Assume that any two organisms can mate.

Sample Dataset

2 2 2

Sample Output

0.78333
"""

from docopt import docopt


def get_k_m_n(inp_file):
    with open(inp_file, 'r') as inp:
        k, m, n = inp.readline().strip().split(' ')
    return float(k), float(m), float(n)


#TODO: Write elegant, general solution to "marbles-in-jar problem"
def calculate(k, m, n):
    first_pop = k + m + n
    second_pop = first_pop - 1
    kk = k / first_pop * (k - 1) / second_pop
    km = k / first_pop * (m) / second_pop + m / first_pop * (k) / second_pop
    kn = k / first_pop * (n) / second_pop + n / first_pop * (k) / second_pop
    mm = m / first_pop * (m - 1) / second_pop
    mn = m / first_pop * (n) / second_pop + n / first_pop * (m) / second_pop
    nn = n / first_pop * (n - 1) / second_pop
    return kk, km, kn, mm, mn, nn


def main():
    k, m, n = get_k_m_n(arguments['<input>'])
    #k is homozygous dominant, m heterozygous, and n is homozygous recessive
    #There are 6 possible combinations of parentage, though some may not be
    #possible if there are only 1 individuals of a type
    kk, km, kn, mm, mn, nn = calculate(k, m, n)
    certain = kk + km + kn
    three_quarter = 0.75 * mm
    half = 0.5 * mn
    print(certain + three_quarter + half)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()
