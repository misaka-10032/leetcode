# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.numIslands2(0, 0, []) == []
    assert sol.numIslands2(1, 1, [[0, 0]]) == [1]


def test_1():
    pos = [[0, 0], [0, 1], [1, 2], [2, 1]]
    assert sol.numIslands2(3, 3, pos) == [1, 1, 2, 3]
