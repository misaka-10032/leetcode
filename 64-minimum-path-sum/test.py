# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minPathSum([]) == 0
    assert sol.minPathSum([[]]) == 0
    assert sol.minPathSum([[2]]) == 2


def test_1():
    sol = Solution()
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert sol.minPathSum(grid) == 21
