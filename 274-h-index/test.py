# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    assert sol.hIndex([]) == 0
    assert sol.hIndex([2]) == 1
    assert sol.hIndex([1, 2]) == 1
    assert sol.hIndex([2, 2]) == 2


def test_1():
    assert sol.hIndex([3, 0, 6, 1, 5]) == 3
    assert sol.hIndex([23, 32, 34, 45, 65, 65]) == 6
    assert sol.hIndex([28, 14, 5, 5, 5, 4, 3,
                       2, 2, 2, 2, 2, 1, 1, 1]) == 5
