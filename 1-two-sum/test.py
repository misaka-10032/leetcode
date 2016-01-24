# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([15, 1, 11, 7, 2], 18) == [3, 4]
