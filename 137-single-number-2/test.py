# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.singleNumber([]) == 0


def test_1():
    sol = Solution()
    assert sol.singleNumber([1, 2, 2, 3, 2, 1, 1]) == 3
    assert sol.singleNumber([1, 2, 2, 3, 2, 1, 1, 3]) == 3
