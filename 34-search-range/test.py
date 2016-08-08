# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.searchRange([], 1) == [-1, -1]
    assert sol.searchRange([1], 1) == [0, 0]
    assert sol.searchRange([100], 1) == [-1, -1]


def test_1():
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert sol.searchRange([5, 7, 7, 8, 8, 10, 10], 5) == [0, 0]
    assert sol.searchRange([5, 7, 7, 8, 8, 10, 10], 10) == [5, 6]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
