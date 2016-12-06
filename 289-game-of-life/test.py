# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    b = [[]]
    sol.gameOfLife(b)
    assert b == [[]]

    b = [[0]]
    sol.gameOfLife(b)
    assert b == [[0]]

    b = [[1]]
    sol.gameOfLife(b)
    assert b == [[0]]


def test_1():
    b = [[0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [1, 1, 1, 1, 1]]
    sol.gameOfLife(b)
    assert b == [[0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 0],
                 [1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1]]
