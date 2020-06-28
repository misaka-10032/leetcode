# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minimumTotal([]) == 0
    assert sol.minimumTotal([[2]]) == 2


def test_1():
    sol = Solution()
    triangle = [[2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]]
    assert sol.minimumTotal(triangle) == 11
