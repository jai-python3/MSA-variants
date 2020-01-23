#!/usr/bin/env python3

from Bio import AlignIO
y=0
alignment = AlignIO.read("MSA_13.fas", "fasta")
for r in range(0,len(alignment[12].seq)):
    if alignment[0,r] == "-" or alignment[1,r] == "-" or alignment[2,r] == "-" or alignment[3,r] == "-" or alignment[4,r] == "-" or alignment[5,r] == "-" or alignment[6,r] == "-" or alignment[7,r] == "-" or alignment[8,r] == "-" or alignment[9,r] == "-" or alignment[10,r] == "-" or alignment[11,r] == "-" or alignment[12,r] == "-":
      y=y+1
      print r+1, alignment[0,r], alignment[1,r], alignment[2,r], alignment[3,r], alignment[4,r], alignment[5,r], alignment[6,r], alignment[7,r], alignment[8,r], alignment[9,r], alignment[10,r], alignment[11,r], alignment[12,r]
    else:
             y=0
