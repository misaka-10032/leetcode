# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    assert sol.findPeakElement([0]) == 0
    assert sol.findPeakElement([1, 2]) == 1

def test_1():
    assert sol.findPeakElement([1, 2, 3, 1]) == 2
    assert sol.findPeakElement([1, 2, 3, 4, 5, 6, 5, 4, 2]) == 5
    assert sol.findPeakElement([0, 1, 2, 3, 4, 5, 6, 7]) == 7
    assert sol.findPeakElement([7, 6, 5, 4, 3, 2, 1, 0]) == 0
