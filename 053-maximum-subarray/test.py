# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.maxSubArray([]) == 0
    assert sol.maxSubArray([2]) == 2
    assert sol.maxSubArray([-2, -3, -4]) == -2


def test_1():
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_2():
    sol = Solution()
    assert sol.maxSubArray([-1]) == -1
