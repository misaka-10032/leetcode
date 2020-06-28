# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution

def test_0():
    sol = Solution()
    assert sol.myPow(10, 0) == 1


def test_1():
    sol = Solution()
    for _ in xrange(100):
        x = (np.random.rand() - .5) * 10
        n = np.random.randint(-100, 100)
        assert abs(x**n - sol.myPow(x, n)) / x**n < 1e-4
