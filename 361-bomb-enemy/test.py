# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.maxKilledEnemies([[]]) == 0
    assert sol.maxKilledEnemies([['E']]) == 0
    assert sol.maxKilledEnemies([['0', 'E']]) == 1


def test_1():
    grid = [['0', 'E', '0', '0'],
            ['E', '0', 'W', 'E'],
            ['0', 'E', '0', '0']]
    assert sol.maxKilledEnemies(grid) == 3
