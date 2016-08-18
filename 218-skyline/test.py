# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.getSkyline([]) == []
    assert sol.getSkyline([[2, 9, 10]]) == [[2, 10], [9, 0]]


def test_1():
    sol = Solution()
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                 [15, 20, 10], [19, 24, 8]]
    tgt = [[2, 10], [3, 15], [7, 12], [12, 0],
           [15, 10], [20, 8], [24, 0]]
    assert sol.getSkyline(buildings) == tgt


def test_2():
    sol = Solution()
    buildings = [[2, 4, 7], [2, 4, 5], [2, 4, 6]]
    tgt = [[2, 7], [4, 0]]
    assert sol.getSkyline(buildings) == tgt
