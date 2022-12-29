#!/usr/bin/env python

# https://numba.pydata.org/

import numba
import numpy as np
from numba import njit
from numba import njit
import time
import random


def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


@njit
def monte_carlo_pi_njit(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


@njit(parallel=True)
def logistic_regression(Y, X, w, iterations):
    for i in range(iterations):
        w -= np.dot(((1.0 / (1.0 + np.exp(-Y * np.dot(X, w))) - 1.0) * Y), X)
    return w


"""compare the use of numba with regular python"""

print(f"numba v:{numba.__version__}")
times = 10000000
for f in [monte_carlo_pi, monte_carlo_pi_njit]:
    start = time.time()
    f(times)
    end = time.time()
    print(f"{f}({times}) done in {end - start}s")
