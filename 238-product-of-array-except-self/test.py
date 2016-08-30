# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_1():
    sol = Solution()
    for n in xrange(2, 21):
        a = np.random.choice(range(1, 10), n).tolist()
        p = np.prod(a)
        tgt = [p//x for x in a]
        assert sol.productExceptSelf(a) == tgt
