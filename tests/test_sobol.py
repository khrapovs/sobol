#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing suite for Sobol random-number generator.

"""
from __future__ import print_function, division

import unittest as ut

from sobol import sobol_rvs


class SobolTestCase(ut.TestCase):
    """Test Sobol."""

    def test_float(self):
        """Test single dimensions."""
        size = 1
        rvs = sobol_rvs(size=size)
        self.assertEqual(rvs.size, 1)

    def test_single_dimensions(self):
        """Test single dimensions."""
        sizes = [2, 100]

        for size in sizes:
            rvs = sobol_rvs(size=size)
            self.assertEqual(rvs.shape[0], size)

    def test_double_dimensions(self):
        """Test double dimensions."""
        sizes = [(2, 100), (40, 2)]

        for size in sizes:
            rvs = sobol_rvs(size=size)
            self.assertEqual(rvs.shape, size)

    def test_exception(self):
        """Test too large dimensions."""
        size = (41, 1)
        fun = lambda: sobol_rvs(size=size)
        self.assertRaises(ValueError, fun)


if __name__ == '__main__':
    ut.main()
