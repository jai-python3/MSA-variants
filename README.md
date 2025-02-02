# MSA-variants
Detection of SNPs and InDels from a Multiple Sequence Alignment file in FASTA format.

- [MSA-variants](#msa-variants)
  - [Use Cases](#use-cases)
  - [Class Diagram](#class-diagram)
  - [INDELs](#indels)
  - [SNPs](#snps)
  - [Usage:](#usage)
    - [Clone the code:](#clone-the-code)
    - [Create your virtual Python environment](#create-your-virtual-python-environment)
    - [Build the code and then install msa\_variant package locally:](#build-the-code-and-then-install-msa_variant-package-locally)
    - [Test the code using the example multiple sequence alignment Ensembl Peason file provided:](#test-the-code-using-the-example-multiple-sequence-alignment-ensembl-peason-file-provided)
    - [To only extract SNPs:](#to-only-extract-snps)
    - [To only extract indels:](#to-only-extract-indels)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [License](#license)

## Use Cases

![use case diagram](use_case.png)

## Class Diagram

![class diagram](class_diagram.png)


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

### Create your virtual Python environment

```shell
cd MSA-variants
virtualenv -p python3 venv
source venv/bin/activate
```

### Build the code and then install msa_variant package locally:

```shell
python setup.py sdist
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Planned improvements are listed here:<br>
[TODO](TODO.md)

## License

License information is available here:<br>
[GNU GENERAL PUBLIC LICENSE](LICENSE)
