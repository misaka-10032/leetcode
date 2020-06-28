# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.maxProduct([]) == 0
    assert sol.maxProduct([-1]) == -1
    assert sol.maxProduct([2]) == 2
    assert sol.maxProduct([-1, 2]) == 2


def test_1():
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-1, 0, -2, 0, -3, 0]) == 0
    assert sol.maxProduct([-1, 0, -2, 0, 1]) == 1
    assert sol.maxProduct([1, 2, 3, -2, 2, -2, 0]) == 48
