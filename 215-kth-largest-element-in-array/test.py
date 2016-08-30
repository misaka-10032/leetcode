# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_1():
    sol = Solution()
    for n in xrange(1, 100):
        a = np.random.choice(100, n).tolist()
        b = sorted(a)
        k = 1 + np.random.randint(n)
        assert sol.findKthLargest(a, k) == b[-k]


def test_2():
    sol = Solution()
    assert sol.findKthLargest([2, 1], 1) == 2
