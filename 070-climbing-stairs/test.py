# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def ref(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    for i in xrange(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


def test_1():
    sol = Solution()
    for n in xrange(100):
        assert ref(n) == sol.climbStairs(n)
