# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.shortestDistance([[]]) == -1
    assert sol.shortestDistance([[1]]) == -1
    assert sol.shortestDistance([[1, 0]]) == 1
    assert sol.shortestDistance([[1, 2, 0]]) == -1


def test_1():
    grid = [[1, 0, 2, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]]
    assert sol.shortestDistance(grid) == 7
