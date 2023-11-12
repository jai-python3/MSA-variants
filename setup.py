#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "Rich", "PyYAML", "biopython"]

test_requirements = []

setup(
    author="Jaideep Sundaram",
    author_email="jai.python3@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Detection of SNPs and InDels from a Multiple Sequence Alignment file",
    entry_points={
        "console_scripts": [
            "msa_variants=msa_variants.msa_variants:main",
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="msa_variants",
    name="msa_variants",
    packages=find_packages(include=["msa_variants", "msa_variants.*"]),
    package_data={"msa_variants": ["conf/config.yaml"]},
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jai-python3/MSA-variants",
    version="0.1.0",
    zip_safe=False,
)
