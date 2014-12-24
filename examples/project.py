#!/usr/bin/env python
# from numpy import sqrt, sum
#from random import normalvariate
from math import *
from scipy.stats import norm
from sobol import *

#y=normalvariate(0,1)

#i4_sobol_generate(2,1000,3).transpose()
f=i4_sobol_generate(2,1000,3).transpose()
#y=norm.ppf(self.u[self.f,0])
 

def MC(nn):
    mean=0.0
    var=0.0
#        t1_avr=
    for i1 in range(nn):          
        u=f[i1][0]
        y=norm.ppf(u)
        mean+=y
        var+=y*y        
    return (mean/nn,var/nn)

n = 1000
print MC(n)

R = norm.rvs(size=n)

print (mean(R), var(R))