# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import math
from solution import Solution


def test_0():
    sol = Solution()
    assert not sol.permuteUnique([])


def test_1():
    sol = Solution()
    nums = [1, 2, 3]
    ans = [[1, 2, 3], [1, 3, 2],
           [2, 1, 3], [2, 3, 1],
           [3, 1, 2], [3, 2, 1]]
    assert sorted(ans) == sorted(sol.permuteUnique(nums))


def test_2():
    sol = Solution()
    nums = [1, 1, 2]
    ans = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert sorted(ans) == sorted(sol.permuteUnique(nums))


def test_3():
    sol = Solution()
    nums = [2, 2, 1, 1]
    ans = [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1],
           [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
    assert sorted(ans) == sorted(sol.permuteUnique(nums))
