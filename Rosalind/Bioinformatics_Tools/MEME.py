#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""New Motif Discovery

Usage:
  MEME.py <input>
  MEME.py (--help | --version)

Options:
  -h --help       show this help message and exit
  -v --version    show version and exit

This script is simply a pythonic encapsulation of a locally installed MEME. It
"""

problem_description = """New Motif Discovery

Problem

The novel-motif finding tool MEME can be found here:
http://meme.nbcr.net/meme/cgi-bin/meme.cgi

Given: A set of protein strings in FASTA format that share some motif with
minimum length 20.

Return: Regular expression for the best-scoring motif.

Sample Dataset

>Rosalind_7142
PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQ
FYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFE
WGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNM
SYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY
>Rosalind_4494
VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERY
PIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADF
QRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFL
KTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM
>Rosalind_3636
ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCF
NKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMA
GNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMM
GHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN

Sample Output

DLWWCWIPVHK[NK]PHSFLKTWSPAAGHRGWQFDHNFF
"""

from docopt import docopt
import subprocess


def main():
    proc = subprocess.Popen(['meme', arguments['<input>'],
                             '-text', '-minw', '20'],
                            stdout=subprocess.PIPE)
    output = proc.stdout.read()
    lines = output.split('\n')
    for line in lines:
        if 'Motif 1 regular expression' == line.strip():
            print(lines[lines.index(line) + 2])
            break

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main()