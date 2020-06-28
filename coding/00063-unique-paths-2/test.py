# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.uniquePathsWithObstacles([]) == 0
    assert sol.uniquePathsWithObstacles([[0, 0, 0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 1, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0], [0], [0]]) == 1
    assert sol.uniquePathsWithObstacles([[0], [1], [0]]) == 0


def test_1():
    sol = Solution()
    grid = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    assert sol.uniquePathsWithObstacles(grid) == 2


def test_2():
    sol = Solution()
    grid = [[0]]
    assert sol.uniquePathsWithObstacles(grid) == 1
