# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.numIslands([]) == 0
    assert sol.numIslands([[]]) == 0


def test_1():
    grid = [['0', '0', '0', '0'],
            ['0', '1', '1', '0'],
            ['0', '0', '1', '0'],
            ['0', '1', '0', '0']]
    sol = Solution()
    assert sol.numIslands(grid) == 2


def test_2():
    grid = [['0', '1', '0'],
            ['0', '1', '0'],
            ['0', '1', '0']]
    sol = Solution()
    assert sol.numIslands(grid) == 1
