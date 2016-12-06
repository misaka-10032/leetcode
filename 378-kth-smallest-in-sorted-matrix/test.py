# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    assert sol.kthSmallest(matrix, 8) == 13
