#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compare means and variances of Scipy and Sobol random numbers.

"""
import numpy as np
from scipy.stats import norm, uniform
from sobol import sobol_rvs
import matplotlib.pylab as plt
import seaborn as sns


def plot_normals():
    """Plot normal densities.

    """
    size, skip = 100, 10

    unif = sobol_rvs(size=size, skip=skip)
    normals_sobol = norm.ppf(unif)
    normals_scipy = norm.rvs(size=size)

    clip = 4
    grid = np.linspace(-clip, clip, 100)
    sns.kdeplot(normals_sobol, shade=True, label='Sobol')
    sns.kdeplot(normals_scipy, shade=True, label='Scipy')
    plt.plot(grid, norm.pdf(grid), label='Normal')
    plt.legend()
    plt.show()


def plot_uniforms():
    """Plot uniform random numbers.

    """
    size, skip = (2, 100), 10
    unif_sobol = sobol_rvs(size=size, skip=skip)
    unif_scipy = uniform.rvs(size=size)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    axes[0].scatter(unif_sobol[0], unif_sobol[1], color='blue')
    axes[1].scatter(unif_scipy[0], unif_scipy[1], color='red')
    axes[0].set_title('Sobol')
    axes[1].set_title('Scipy')
    for ax in axes:
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
    plt.savefig('../docs/source/_static/uniforms.png')
    plt.show()


if __name__ == '__main__':
    plot_uniforms()
    plot_normals()
