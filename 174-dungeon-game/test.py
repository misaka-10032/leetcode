# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.calculateMinimumHP([]) == 0
    assert sol.calculateMinimumHP([[]]) == 0
    assert sol.calculateMinimumHP([[2]]) == 1
    assert sol.calculateMinimumHP([[-2]]) == 3


def test_1():
    sol = Solution()
    a = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]
    assert sol.calculateMinimumHP(a) == 7
