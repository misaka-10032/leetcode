# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_0():
    sol = Solution()
    a = []
    sol.sortColors([])
    assert a == []


def test_1():
    sol = Solution()
    for n in xrange(100):
        a = np.random.choice(3, n).tolist()
        tgt = sorted(a)
        sol.sortColors(a)
        assert a == tgt
