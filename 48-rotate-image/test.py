# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def rotate(a):
    n = len(a)
    b = [[0]*n for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            b[j][n-i-1] = a[i][j]
    return b


def test():
    sol = Solution()
    for n in xrange(1, 100):
        a = np.random.randint(0, 100, (n, n)).tolist()
        b = rotate(a)
        sol.rotate(a)
        assert a == b
