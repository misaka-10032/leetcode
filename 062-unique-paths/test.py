# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.uniquePaths(0, 0) == 0
    assert sol.uniquePaths(2, 0) == 0
    assert sol.uniquePaths(0, 2) == 0
    assert sol.uniquePaths(1, 3) == 1
    assert sol.uniquePaths(3, 1) == 1


def test_1():
    sol = Solution()
    assert sol.uniquePaths(3, 3) == 6
    assert sol.uniquePaths(3, 5) == 15
