# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import NumMatrix


def test_0():
    m = [[1]]
    sol = NumMatrix(m)
    assert sol.sumRegion(0, 0, 0, 0) == 1
    sol.update(0, 0, 2)
    assert sol.sumRegion(0, 0, 0, 0) == 2


def test_1():
    m = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
    sol = NumMatrix(m)
    assert sol.sumRegion(1, 2, 2, 4) == 6
    sol.update(2, 3, 3)
    sol.update(1, 4, 3)
    sol.update(3, 3, 4)
    assert sol.sumRegion(1, 2, 2, 4) == 10
