#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compare means and variances of uniform and Sobol random numbers.

"""
from math import *
import numpy as np
from scipy.stats import norm
from sobol import i4_sobol_generate

#y=normalvariate(0,1)

#i4_sobol_generate(2,1000,3).transpose()
f = i4_sobol_generate(2, 1000, 3).transpose()
#y=norm.ppf(self.u[self.f,0])


def MC(nn):
    mean, var = 0, 0
    for i1 in range(nn):
        u = f[i1][0]
        y = norm.ppf(u)
        mean += y
        var += y*y
    return (mean/nn, var/nn)

n = 1000
print(MC(n))

R = norm.rvs(size=n)

print((np.mean(R), np.var(R)))