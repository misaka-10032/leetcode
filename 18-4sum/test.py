# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test_1():
    sol = Solution()
    nums, target = [1, 0, -1, 0, -2, 2], 0
    ans = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]]
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)
    nums, target = [0, 0, 0, 0], 0
    ans = [[0, 0, 0, 0]]
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)
    nums, target = [0, 1, 2], 0
    ans = []
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)
    nums, target = [1, -1, -1, 0], -1
    ans = [[-1, -1, 0, 1]]
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)

def test_2():
    sol = Solution()
    nums, target = [-3, -2, -1, 0, 0, 1, 2, 3], 0
    ans = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
           [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)
    nums, target = [-7, -5, 0, 7, 1, 1, -10, -2, 7, 7, -2, -6, 0, -10, -5, 7, -8, 5], 28
    ans = [[7, 7, 7, 7]]
    assert sorted(sol.fourSum(nums, target)) == sorted(ans)
