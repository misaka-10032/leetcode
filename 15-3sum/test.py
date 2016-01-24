# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def _assert_eq(s1, s2):
    assert sorted(map(tuple, s1)) == sorted(map(tuple, s2))


def test_1():
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    s = [[-1, 0, 1], [-1, -1, 2]]
    _assert_eq(sol.threeSum(nums), s)
    nums = [1, 2, 3, 4, 5]
    s = []
    _assert_eq(sol.threeSum(nums), s)


def test_2():
    sol = Solution()
    nums = [0, 0, 0, 0]
    s = [[0, 0, 0]]
    _assert_eq(sol.threeSum(nums), s)
    nums = [1, -1, -1, 0]
    s = [[-1, 0, 1]]
    _assert_eq(sol.threeSum(nums), s)
