#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""

Sobol pseudo-random number generator
====================================

.. image:: _static/uniforms.png

Original authors
----------------
    - Original FORTRAN77 version by Bennett Fox
    - Original MATLAB version by John Burkardt
    - Original PYTHON version by Corrado Chisari

Original code: http://people.sc.fsu.edu/~jburkardt/py_src/sobol/sobol.html

Functions
---------

"""
from __future__ import print_function, division

import numpy as np

from .helper_functions import i4_sobol

__author__ = "Stanislav Khrapov"
__email__ = "khrapovs@gmail.com"
__all__ = ['sobol_rvs']


def sobol_rvs(size=10, skip=10):
    r"""Generates a Sobol pseudo-random dataset.

    Parameters
    ----------
    size : int or tuple
        Size of the output array.
        If tuple, then the second dimension is bounded by 40.
    skip : int
        Number of initial points to skip

    Returns
    -------
    array
        Random numbers

    Raises
    ------
    ValueError

    Examples
    --------
    >>> from sobol import sobol_rvs
    >>> rvs = sobol_rvs(size=(2, 3), skip=1000)
    >>> print(rvs)
    [[ 0.15722656  0.21972656  0.71972656]
     [ 0.90917969  0.09667969  0.59667969]]

    """
    if isinstance(size, int):
        m, n = 1, size
    else:
        m, n = size
        if m > 40 or m < 1:
            msg = 'Spacial dimension should be smaller than 40!'
            raise ValueError(msg)
    r = np.zeros((m, n))
    for j in range(n):
        seed = skip + j - 1
        [r[:m, j], seed] = i4_sobol(m, seed)
    return r.squeeze()
