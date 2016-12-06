# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    sol = Solution()
    assert not sol.searchMatrix([[]], 1)
    assert sol.searchMatrix([[1]], 1)
    assert not sol.searchMatrix([[1]], 2)


def test_1():
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    assert sol.searchMatrix(matrix, 1)
    assert sol.searchMatrix(matrix, 7)
    assert sol.searchMatrix(matrix, 23)
    assert sol.searchMatrix(matrix, 50)
    assert sol.searchMatrix(matrix, 11)
    assert not sol.searchMatrix(matrix, 0)
    assert not sol.searchMatrix(matrix, 64)
    assert not sol.searchMatrix(matrix, 12)
    assert not sol.searchMatrix(matrix, 2)
    assert not sol.searchMatrix(matrix, 49)
