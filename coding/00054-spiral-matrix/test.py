# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.spiralOrder([[]]) == []
    assert sol.spiralOrder([[0]]) == [0]
    assert sol.spiralOrder([[1, 2]]) == [1, 2]


def test_1():
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    t = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert sol.spiralOrder(m) == t


def test_2():
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    t = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert sol.spiralOrder(m) == t


def test_3():
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]
    t = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    assert sol.spiralOrder(m) == t


def test_4():
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    t = [1, 2, 3, 4, 8, 12, 16, 15,
         14, 13, 9, 5, 6, 7, 11, 10]
    assert sol.spiralOrder(m) == t
