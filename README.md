# MSA-variants
Detection of SNPs and InDels from a Multiple Sequence Alignment file in FASTA format.

## INDELs

Will write an `indels.txt` file that will indicate the following:
* number of indels
* location (POS) 
* sequences in the following lines

```
# Number of indels: '8'
POS       	1 2 3 5 6 11 15 20
seq1      	c t g t - - - a 
seq2      	- t g t - t a - 
seq3       	c - - - c t a a
```

## SNPs

Will write a `snps.txt` file that will indicate the following:
* number of SNPs
* location (POS) 
* sequences in the following lines

```
# Number of SNPs: '7'
POS       	133 225 309 346 391 746 793
seq1      	c g a t c g a 
seq2      	c g a c g - a 
seq3       	t a c c c a g 
```

## Usage:

### Clone the code:

```shell
mkdir -p ${HOME}/projects
cd ${HOME}/projects
git clone https://github.com/jai-python3/MSA-variants.git
```

### Build the code:

```shell
cd MSA-variants
pip uninstall msa_variants ; make clean ; python setup.py sdist
```

### Create your virtual Python environment and then install msa_variant package locally:

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install .
```

### Test the code using the example multiple sequence alignment Ensembl Peason file provided:

```shell
msa_variants --infile ensembl_peasron.fsa 
```


### To only extract SNPs:

```shell
msa_variants --infile ensembl_peasron.fsa --snps-only
```

### To only extract indels:

```shell
msa_variants --infile ensembl_peasron.fsa --indels-only
```

