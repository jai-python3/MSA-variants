# MSA-variants
Detection of SNPs and InDels from a Multiple Sequence Alignment file

### Input:
A multiple alignment file in fasta format

### Usage:
    ./Extract_InDels_from_MSA.py input.fas

> produces a `indels.txt` file with no. of InDels in the first line and InDel location (POS) and sequences in the following lines
```
# Number of InDels: 8
POS       	1 2 3 5 6 11 15 20
seq1      	c t g t - - - a 
seq2      	- t g t - t a - 
seq3       	c - - - c t a a
```


    ./Extract_SNPs_from_MSA.py input.fas 

> produces a `snps.txt` file with no. of SNPs in the first line and SNP location (POS) and sequences in the following lines
```
# Number of SNPs: 7
POS       	133 225 309 346 391 746 793
seq1      	c g a t c g a 
seq2      	c g a c g - a 
seq3       	t a c c c a g 
```

