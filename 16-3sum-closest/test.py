# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test_1():
    sol = Solution()
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert sol.threeSumClosest([1, 1, 2, 2, 3, 3, 4, 4], 7) == 7
    assert sol.threeSumClosest([1, 1, 2, 2, 3, 3, 4, 4], 12) == 11
    assert sol.threeSumClosest([1, 1, 2, 2, 3, 3, 4, 4], 3) == 4
