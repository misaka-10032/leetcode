# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.maxProfit([]) == 0
    assert sol.maxProfit([2]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0


def test_1():
    sol = Solution()
    assert sol.maxProfit([9, 6, 8, 2, 7]) == 5
