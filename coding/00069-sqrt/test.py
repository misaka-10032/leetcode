# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    for i in xrange(100):
        assert sol.mySqrt(i*i) == i


def test_2():
    sol = Solution()
    assert 46339 <= sol.mySqrt(2147395599) <= 46340
