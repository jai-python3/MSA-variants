"""
Copyright (c) 2023 Jaideep Sundaram

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""


from Bio import AlignIO

import logging
import os
from datetime import datetime
from typing import List


DEFAULT_VERBOSE = False
DEFAULT_IDENTIFIER_PADDING = 30
DEFAULT_IDENTIFIER_SUBSTRING_LENGTH = 20


class Extractor:
    """Class for extracting indels and/or SNPs from multiple sequence alignment."""

    def __init__(self, **kwargs):
        """Constructor for Extractor"""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", None)
        self.verbose = kwargs.get("verbose", DEFAULT_VERBOSE)
        self.indels_only = kwargs.get("indels_only", False)
        self.snps_only = kwargs.get("snps_only", False)
        self.identifier_padding = int(
            self.config.get("identifier_padding", DEFAULT_IDENTIFIER_PADDING)
        )
        self.identifier_substring_length = int(
            self.config.get(
                "identifier_substring_length", DEFAULT_IDENTIFIER_SUBSTRING_LENGTH
            )
        )

        if self.identifier_substring_length >= self.identifier_padding:
            self.identifier_padding = self.identifier_substring_length + (
                self.identifier_substring_length - self.identifier_padding
            )
            logging.info(
                f"Setting identifier_padding to '{self.identifier_padding}' because identifier_substring_length is '{self.identifier_substring_length}'"
            )

        logging.info(f"Instantiated Extractor in file '{os.path.abspath(__file__)}'")

    def extract(self, infile: str) -> None:
        """Extract the SNPs and the indels from the multiple sequence alignment.

        Args:
            infile (str): the multiple sequence alignment file
        """
        if not self.indels_only:
            self.extract_snps(infile)

        if not self.snps_only:
            self.extract_indels(infile)

    def extract_snps(self, infile) -> None:
        """Extract the SNPs from the multiple sequence alignment.

        Args:
            infile (str): the multiple sequence alignment file
        """
        logging.info(
            f"Will attempt to extract SNPs from multiple sequence alignment file '{infile}'"
        )

        snp_ctr = 0
        snp_list = []

        alignment = AlignIO.read(infile, "fasta")

        for r in range(0, alignment.get_alignment_length()):
            d = set([record.seq[r] for record in alignment])

            d.discard("-")

            if len(d) > 1:
                snp_list.append(r)
                snp_ctr += 1

        self._write_snp_outfile(alignment, infile, snp_ctr, snp_list)

    def _write_snp_outfile(
        self, alignment, infile: str, snp_ctr: int, snp_list: List[int]
    ) -> None:
        """Write the SNPs to the output file.

        Args:
            alignment (object): alignment object from biopython
            infile (str): the input file
            snp_ctr (int): the number of SNPs counted
            snp_list (list): the positions of the encountered SNPs

        """
        outfile = os.path.join(self.outdir, "snps.txt")

        with open(outfile, "w") as out_file_handle:
            if self.config["include_provenance"]:
                out_file_handle.write(
                    f"## method-created: {os.path.abspath(__file__)}\n"
                )
                out_file_handle.write(
                    f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n"
                )
                out_file_handle.write(f"## created-by: {os.environ.get('USER')}\n")
                out_file_handle.write(f"## config_file: {self.config_file}\n")
                out_file_handle.write(f"## infile: {infile}\n")
                out_file_handle.write(f"## logfile: {self.logfile}\n")

            out_file_handle.write(f"## Number of SNPs: '{snp_ctr}'\n")

            out_file_handle.write(
                f"{'POS:':<{self.identifier_padding}}{' '.join(str(i+1) for i in snp_list)}\n"
            )

            for record in alignment:
                out_file_handle.write(
                    f"{record.id[:self.identifier_substring_length]:<{self.identifier_padding}}"
                )
                for i in snp_list:
                    out_file_handle.write(f"{record.seq[i]} ")
                out_file_handle.write("\n")

        logging.info(f"Wrote SNP output file '{outfile}'")
        if self.verbose:
            print(f"Wrote SNP output file '{outfile}'")

    def extract_indels(self, infile: str) -> None:
        """Extract the indels from the multiple sequence alignment.

        Args:
            infile (str): the multiple sequence alignment file
        """
        logging.info(
            f"Will attempt to extract indels from multiple sequence alignment file '{infile}'"
        )

        indel_ctr = 0
        indel_list = []

        alignment = AlignIO.read(infile, "fasta")

        for r in range(0, alignment.get_alignment_length()):
            if any(record.seq[r] == "-" for record in alignment):
                indel_list.append(r)

                indel_ctr += 1

        self._write_indels_outfile(alignment, infile, indel_ctr, indel_list)

    def _write_indels_outfile(
        self, alignment, infile: str, indel_ctr: int, indel_list: List[int]
    ) -> None:
        """Write the indels to the output file.

        Args:
            alignment (object): alignment object from biopython
            infile (str): the input file
            indel_ctr (int): the number of indels counted
            indel_list (list): the positions of the encountered indels

        """
        outfile = os.path.join(self.outdir, "indels.txt")

        with open(outfile, "w") as out_file_handle:
            if self.config["include_provenance"]:
                out_file_handle.write(
                    f"## method-created: {os.path.abspath(__file__)}\n"
                )
                out_file_handle.write(
                    f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n"
                )
                out_file_handle.write(f"## created-by: {os.environ.get('USER')}\n")
                out_file_handle.write(f"## config_file: {self.config_file}\n")
                out_file_handle.write(f"## infile: {infile}\n")
                out_file_handle.write(f"## logfile: {self.logfile}\n")

            out_file_handle.write(f"## Number of indels: '{indel_ctr}'\n")

            out_file_handle.write(
                f"{'POS:':<{self.identifier_padding}}{' '.join(str(i+1) for i in indel_list)}\n"
            )

            for record in alignment:
                out_file_handle.write(
                    f"{record.id[:self.identifier_substring_length]:<{self.identifier_padding}}"
                )
                for i in indel_list:
                    out_file_handle.write(f"{record.seq[i]} ")
                out_file_handle.write("\n")

        logging.info(f"Wrote indels output file '{outfile}'")
        if self.verbose:
            print(f"Wrote indels output file '{outfile}'")
