#!/usr/bin/env python3

# Extract_SNPs_from_MSA.py input.fas 

# Copyright (c) 2022 Sai Reddy Achakkagari

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import sys
from Bio import AlignIO
y=0
snp=[]
alignment = AlignIO.read(sys.argv[1], "fasta")
for r in range(0,alignment.get_alignment_length()):
    d=set([record.seq[r] for record in alignment])
    d.discard('-')
    if len(d)>1:
        snp.append(r)
        y+=1
with open("snps.txt",'w') as out:   
    print('# Number of SNPs:', y,file=out)
    print('POS'.ljust(10),end='\t',file=out)
    print(" ".join(str(i+1) for i in snp),file=out)
    for record in alignment:
        print(record.id[:10].ljust(10),end='\t',file=out)
        for i in snp:
            print(record.seq[i],end=' ',file=out)  
        print(file=out)

