# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.largestRectangleArea([]) == 0
    assert sol.largestRectangleArea([3]) == 3
    assert sol.largestRectangleArea([2, 3]) == 4
    assert sol.largestRectangleArea([3, 2]) == 4
    assert sol.largestRectangleArea([2, 2, 3]) == 6
    assert sol.largestRectangleArea([3, 2, 3]) == 6


def test_1():
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    assert sol.largestRectangleArea(heights) == 10


def test_2():
    sol = Solution()
    heights = [0, 1, 0, 1]
    assert sol.largestRectangleArea(heights) == 1


def test_3():
    sol = Solution()
    heights = [2, 5, 5, 2]
    assert sol.largestRectangleArea(heights) == 10
