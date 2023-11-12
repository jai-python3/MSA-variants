#!/usr/bin/env python

"""Tests for `msa_variants` package."""


import unittest
from click.testing import CliRunner

from msa_variants import msa_variants
from msa_variants import cli


class TestMsa_variants(unittest.TestCase):
    """Tests for `msa_variants` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'msa_variants.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
