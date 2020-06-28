# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    assert sol.numSquares(1) == 1
    assert sol.numSquares(2) == 2
    assert sol.numSquares(3) == 3
    assert sol.numSquares(4) == 1
    assert sol.numSquares(5) == 2
    assert sol.numSquares(6) == 3
    assert sol.numSquares(7) == 4
    assert sol.numSquares(8) == 2
    assert sol.numSquares(12) == 3


def test_2():
    sol = Solution()
    assert sol.numSquares(28) == 4
