# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    assert not sol.searchMatrix([[]], 1)
    assert not sol.searchMatrix([[2]], 1)
    assert sol.searchMatrix([[2]], 2)


def test_1():
    a = [[1,   4,  7, 11, 15],
         [2,   5,  8, 12, 19],
         [3,   6,  9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    assert sol.searchMatrix(a, 1)
    assert sol.searchMatrix(a, 15)
    assert sol.searchMatrix(a, 30)
    assert sol.searchMatrix(a, 18)
    assert sol.searchMatrix(a, 13)
    assert not sol.searchMatrix(a, 32)
    assert not sol.searchMatrix(a, 0)
